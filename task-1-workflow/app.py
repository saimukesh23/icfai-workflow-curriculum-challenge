"""
ICFAI Hyderabad - Sports Court Booking MVP
Storage: plain text files (JSON content) inside ./data  -> no database / SQL.
Roles: administrator, club_head, student
"""
import hashlib
import json
import os
import secrets
import threading
import uuid
from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(page_title="ICFAI Sports Booking", page_icon="🏟️", layout="wide")

TZ = ZoneInfo("Asia/Kolkata")
DATA_DIR = "data"
USERS_F = os.path.join(DATA_DIR, "users.txt")
BOOKINGS_F = os.path.join(DATA_DIR, "bookings.txt")
CLOSURES_F = os.path.join(DATA_DIR, "closures.txt")
SETTINGS_F = os.path.join(DATA_DIR, "settings.txt")

COURTS = ["Volleyball Court", "Basketball Court", "Cricket Ground", "Tennis Court"]
SLOT_MIN = 30          # slot granularity in minutes
MAX_DURATION = 60      # hard rule from the report: max 1 hour per booking
ROLES = {"administrator": "Administrator", "club_head": "Sports Club Head", "student": "Student"}

DEFAULT_SETTINGS = {
    "open_time": "06:00",
    "close_time": "21:00",
    "advance_days": 7,            # how many days ahead students can book
    "max_bookings_per_day": 2,    # per student per day
    "club_contact": "Not set yet (Admin can set this in Settings)",
}

_lock = threading.Lock()


# ----------------------------------------------------------------------------
# TEXT-FILE STORAGE
# ----------------------------------------------------------------------------
def _hash(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode()).hexdigest()


def _read(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _write(path, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)  # atomic replace


def make_user(username, name, role, password):
    salt = secrets.token_hex(8)
    return {"username": username, "name": name, "role": role,
            "salt": salt, "pw": _hash(password, salt)}


def init_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_F):
        # DEFAULT ACCOUNTS - change these passwords after first login!
        _write(USERS_F, [
            make_user("admin", "Administrator", "administrator", "admin123"),
            make_user("clubhead", "Sports Club Head", "club_head", "club123"),
        ])
    if not os.path.exists(BOOKINGS_F):
        _write(BOOKINGS_F, [])
    if not os.path.exists(CLOSURES_F):
        _write(CLOSURES_F, [])
    if not os.path.exists(SETTINGS_F):
        _write(SETTINGS_F, DEFAULT_SETTINGS)


def users():
    return _read(USERS_F, [])


def bookings():
    return _read(BOOKINGS_F, [])


def closures():
    return _read(CLOSURES_F, [])


def settings():
    s = dict(DEFAULT_SETTINGS)
    s.update(_read(SETTINGS_F, {}))
    return s


def now():
    return datetime.now(TZ)


# ----------------------------------------------------------------------------
# TIME HELPERS
# ----------------------------------------------------------------------------
def t_to_min(t: str) -> int:
    h, m = map(int, t.split(":"))
    return h * 60 + m


def min_to_t(m: int) -> str:
    return f"{m // 60:02d}:{m % 60:02d}"


def fmt_date(d: str) -> str:
    return datetime.strptime(d, "%Y-%m-%d").strftime("%a, %d %b %Y")


# ----------------------------------------------------------------------------
# BOOKING LOGIC (rules from the report)
# ----------------------------------------------------------------------------
def active_bookings(court=None, day=None):
    out = [b for b in bookings() if b["status"] == "confirmed"]
    if court:
        out = [b for b in out if b["court"] == court]
    if day:
        out = [b for b in out if b["date"] == day]
    return out


def closure_for(court, day):
    """Return the closure (if any) that blocks this court on this date."""
    for c in closures():
        if c["start_date"] <= day <= c["end_date"] and c["court"] in ("ALL", court):
            return c
    return None


def validate_booking(student_id, court, day, start_min, duration, ignore_limit=False):
    """Returns (ok, message). Applies every rule from the proposal."""
    s = settings()
    if court not in COURTS:
        return False, "Invalid court."
    if duration <= 0 or duration > MAX_DURATION:
        return False, f"A booking can be at most {MAX_DURATION} minutes."
    end_min = start_min + duration
    if start_min < t_to_min(s["open_time"]) or end_min > t_to_min(s["close_time"]):
        return False, f"Courts are open {s['open_time']} - {s['close_time']}."

    d = datetime.strptime(day, "%Y-%m-%d").date()
    start_dt = datetime.combine(d, time(start_min // 60, start_min % 60), tzinfo=TZ)
    if start_dt < now():
        return False, "That slot has already started or passed."
    if d > now().date() + timedelta(days=int(s["advance_days"])):
        return False, f"You can only book up to {s['advance_days']} days ahead."

    c = closure_for(court, day)
    if c:
        return False, f"Closed: {c['reason']}"

    for b in active_bookings(court, day):
        if start_min < t_to_min(b["end"]) and end_min > t_to_min(b["start"]):
            return False, "This slot overlaps with an existing booking."

    if not ignore_limit:
        n = len([b for b in active_bookings(day=day) if b["student_id"] == student_id])
        if n >= int(s["max_bookings_per_day"]):
            return False, f"Daily limit reached ({s['max_bookings_per_day']} bookings per day)."
    return True, "OK"


def create_booking(user, court, day, start_min, duration):
    with _lock:  # re-validate inside lock so two students can't grab the same slot
        ok, msg = validate_booking(user["username"], court, day, start_min, duration)
        if not ok:
            return False, msg, None
        b = {
            "id": uuid.uuid4().hex[:8].upper(),
            "student_id": user["username"],
            "student_name": user["name"],
            "court": court,
            "date": day,
            "start": min_to_t(start_min),
            "end": min_to_t(start_min + duration),
            "status": "confirmed",
            "note": "",
            "created_at": now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        data = bookings()
        data.append(b)
        _write(BOOKINGS_F, data)
        return True, "Booked!", b


def cancel_booking(booking_id, by, note=""):
    with _lock:
        data = bookings()
        for b in data:
            if b["id"] == booking_id and b["status"] == "confirmed":
                b["status"] = "cancelled"
                b["note"] = note or f"Cancelled by {by}"
                b["cancelled_at"] = now().strftime("%Y-%m-%d %H:%M:%S")
                _write(BOOKINGS_F, data)
                return True
        return False


def add_closure(courts, start_d, end_d, reason, by, cancel_existing):
    with _lock:
        data = closures()
        targets = ["ALL"] if set(courts) == set(COURTS) else courts
        for c in targets:
            data.append({
                "id": uuid.uuid4().hex[:8].upper(),
                "court": c, "start_date": start_d, "end_date": end_d,
                "reason": reason, "created_by": by,
                "created_at": now().strftime("%Y-%m-%d %H:%M:%S"),
            })
        _write(CLOSURES_F, data)

        cancelled = 0
        if cancel_existing:
            bk = bookings()
            for b in bk:
                if (b["status"] == "confirmed" and start_d <= b["date"] <= end_d
                        and ("ALL" in targets or b["court"] in targets)):
                    b["status"] = "cancelled"
                    b["note"] = f"Cancelled due to: {reason}"
                    b["cancelled_at"] = now().strftime("%Y-%m-%d %H:%M:%S")
                    cancelled += 1
            _write(BOOKINGS_F, bk)
        return cancelled


def remove_closure(closure_id):
    with _lock:
        _write(CLOSURES_F, [c for c in closures() if c["id"] != closure_id])


def slot_status_table(court, day):
    """Availability grid for one court/day."""
    s = settings()
    rows = []
    c = closure_for(court, day)
    bks = active_bookings(court, day)
    for m in range(t_to_min(s["open_time"]), t_to_min(s["close_time"]), SLOT_MIN):
        label = f"{min_to_t(m)} - {min_to_t(m + SLOT_MIN)}"
        if c:
            status = f"⛔ Closed ({c['reason']})"
        else:
            hit = next((b for b in bks if m < t_to_min(b["end"]) and m + SLOT_MIN > t_to_min(b["start"])), None)
            d = datetime.strptime(day, "%Y-%m-%d").date()
            past = datetime.combine(d, time(m // 60, m % 60), tzinfo=TZ) < now()
            if hit:
                status = "🔴 Booked"
            elif past:
                status = "⚪ Past"
            else:
                status = "🟢 Available"
        rows.append({"Time": label, "Status": status})
    return pd.DataFrame(rows)


def free_starts(user, court, day, duration):
    s = settings()
    out = []
    for m in range(t_to_min(s["open_time"]), t_to_min(s["close_time"]), SLOT_MIN):
        ok, _ = validate_booking(user["username"], court, day, m, duration, ignore_limit=True)
        if ok:
            out.append(m)
    return out


# ----------------------------------------------------------------------------
# AUTH
# ----------------------------------------------------------------------------
def authenticate(username, password):
    for u in users():
        if u["username"].lower() == username.strip().lower():
            if _hash(password, u["salt"]) == u["pw"]:
                return u
    return None


def register_student(roll, name, password):
    roll = roll.strip().upper()
    with _lock:
        data = users()
        if any(u["username"].upper() == roll for u in data):
            return False, "This roll number is already registered."
        data.append(make_user(roll, name.strip(), "student", password))
        _write(USERS_F, data)
    return True, "Registered! You can log in now."


def change_password(username, new_pw):
    with _lock:
        data = users()
        for u in data:
            if u["username"] == username:
                u["salt"] = secrets.token_hex(8)
                u["pw"] = _hash(new_pw, u["salt"])
        _write(USERS_F, data)


# ----------------------------------------------------------------------------
# UI PIECES
# ----------------------------------------------------------------------------
def bookings_df(bks):
    if not bks:
        return pd.DataFrame(columns=["ID", "Student", "Court", "Date", "Time", "Status", "Note"])
    return pd.DataFrame([{
        "ID": b["id"], "Student": f"{b['student_name']} ({b['student_id']})",
        "Court": b["court"], "Date": b["date"],
        "Time": f"{b['start']} - {b['end']}", "Status": b["status"], "Note": b.get("note", ""),
    } for b in sorted(bks, key=lambda x: (x["date"], x["start"]), reverse=True)])


def page_availability(user):
    st.subheader("📅 Court availability")
    s = settings()
    c1, c2 = st.columns(2)
    court = c1.selectbox("Court", COURTS, key="av_court")
    day = c2.date_input("Date", now().date(), min_value=now().date(),
                        max_value=now().date() + timedelta(days=int(s["advance_days"])), key="av_date")
    day_s = day.strftime("%Y-%m-%d")
    cl = closure_for(court, day_s)
    if cl:
        st.error(f"⛔ {court} is closed on {fmt_date(day_s)}: {cl['reason']}")
    st.dataframe(slot_status_table(court, day_s), use_container_width=True, hide_index=True, height=420)


def page_book(user):
    st.subheader("🏐 Book a court")
    s = settings()
    st.caption(f"Max {MAX_DURATION} minutes per booking • Open {s['open_time']} - {s['close_time']} • "
               f"Up to {s['advance_days']} days ahead • {s['max_bookings_per_day']} bookings/day")
    c1, c2, c3 = st.columns(3)
    court = c1.selectbox("Court", COURTS, key="bk_court")
    day = c2.date_input("Date", now().date(), min_value=now().date(),
                        max_value=now().date() + timedelta(days=int(s["advance_days"])), key="bk_date")
    dur = c3.selectbox("Duration", [30, 60], index=1, format_func=lambda x: f"{x} minutes", key="bk_dur")
    day_s = day.strftime("%Y-%m-%d")

    cl = closure_for(court, day_s)
    if cl:
        st.error(f"⛔ {court} is closed on {fmt_date(day_s)}: {cl['reason']}")
        return

    starts = free_starts(user, court, day_s, dur)
    if not starts:
        st.warning("No free slots for this court/date/duration. Try another court or date.")
        return

    start = st.selectbox("Start time", starts,
                         format_func=lambda m: f"{min_to_t(m)} → {min_to_t(m + dur)}", key="bk_start")
    if st.button("✅ Confirm booking", type="primary"):
        ok, msg, b = create_booking(user, court, day_s, start, dur)
        if ok:
            st.success(f"Booking confirmed! ID **{b['id']}** — {b['court']}, {fmt_date(b['date'])}, "
                       f"{b['start']} - {b['end']}. Show this ID if there is a dispute.")
            st.balloons()
        else:
            st.error(msg)


def page_my_bookings(user):
    st.subheader("📋 My bookings")
    mine = [b for b in bookings() if b["student_id"] == user["username"]]
    st.dataframe(bookings_df(mine).drop(columns=["Student"]), use_container_width=True, hide_index=True)
    upcoming = [b for b in mine if b["status"] == "confirmed" and
                datetime.strptime(f"{b['date']} {b['end']}", "%Y-%m-%d %H:%M").replace(tzinfo=TZ) > now()]
    if upcoming:
        pick = st.selectbox("Cancel a booking", upcoming,
                            format_func=lambda b: f"{b['id']} • {b['court']} • {b['date']} {b['start']}-{b['end']}")
        if st.button("Cancel selected booking"):
            cancel_booking(pick["id"], by="student")
            st.success("Cancelled. The slot is free again.")
            st.rerun()
    st.info(f"Disputes / complaints → Sports club contact: **{settings()['club_contact']}** "
            "(share your booking ID).")


def page_all_bookings(user):
    st.subheader("📋 All bookings")
    c1, c2, c3 = st.columns(3)
    f_court = c1.selectbox("Court", ["All"] + COURTS)
    f_status = c2.selectbox("Status", ["All", "confirmed", "cancelled"])
    f_date = c3.text_input("Date (YYYY-MM-DD, optional)")
    bks = bookings()
    if f_court != "All":
        bks = [b for b in bks if b["court"] == f_court]
    if f_status != "All":
        bks = [b for b in bks if b["status"] == f_status]
    if f_date:
        bks = [b for b in bks if b["date"] == f_date.strip()]
    st.dataframe(bookings_df(bks), use_container_width=True, hide_index=True)

    conf = [b for b in bks if b["status"] == "confirmed"]
    if conf:
        pick = st.selectbox("Cancel a booking", conf, format_func=lambda b:
                            f"{b['id']} • {b['student_name']} • {b['court']} • {b['date']} {b['start']}")
        reason = st.text_input("Reason (shown to student)", "Cancelled by sports club")
        if st.button("Cancel this booking"):
            cancel_booking(pick["id"], by=ROLES[user["role"]], note=reason)
            st.success("Booking cancelled.")
            st.rerun()


def page_closures(user):
    st.subheader("🏆 Tournament closures / blocks")
    st.caption("While a closure is active, nobody can book the affected courts on those dates.")

    with st.form("closure_form", clear_on_submit=True):
        reason = st.text_input("Reason", "Inter-college tournament")
        courts = st.multiselect("Courts to block", COURTS, default=COURTS)
        c1, c2 = st.columns(2)
        start = c1.date_input("From", now().date())
        full_week = c2.checkbox("Block the full week (7 days from start)", value=True)
        end_custom = c2.date_input("…or custom end date", now().date() + timedelta(days=6))
        cancel_existing = st.checkbox("Cancel existing bookings in this period", value=True)
        if st.form_submit_button("🚫 Block", type="primary"):
            end = start + timedelta(days=6) if full_week else end_custom
            if not courts:
                st.error("Pick at least one court.")
            elif end < start:
                st.error("End date is before start date.")
            else:
                n = add_closure(courts, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"),
                                reason, user["username"], cancel_existing)
                st.success(f"Blocked {start} → {end}. {n} existing booking(s) cancelled.")
                st.rerun()

    st.markdown("**Current & upcoming closures**")
    cls = sorted(closures(), key=lambda c: c["start_date"])
    if not cls:
        st.info("No closures set.")
    for c in cls:
        col1, col2 = st.columns([5, 1])
        col1.write(f"**{'All courts' if c['court'] == 'ALL' else c['court']}** • "
                   f"{c['start_date']} → {c['end_date']} • {c['reason']} • _by {c['created_by']}_")
        if col2.button("Remove", key="rm_" + c["id"]):
            remove_closure(c["id"])
            st.rerun()


def page_users(user):
    st.subheader("👥 Users")
    df = pd.DataFrame([{"Username": u["username"], "Name": u["name"], "Role": ROLES[u["role"]]} for u in users()])
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("**Add user (e.g., new club head)**")
    with st.form("add_user", clear_on_submit=True):
        c1, c2 = st.columns(2)
        uname = c1.text_input("Username")
        name = c2.text_input("Full name")
        role = c1.selectbox("Role", list(ROLES), format_func=lambda r: ROLES[r], index=1)
        pw = c2.text_input("Password", type="password")
        if st.form_submit_button("Add"):
            if not (uname and name and pw):
                st.error("Fill all fields.")
            elif any(u["username"].lower() == uname.lower() for u in users()):
                st.error("Username exists.")
            else:
                with _lock:
                    data = users()
                    data.append(make_user(uname.strip(), name.strip(), role, pw))
                    _write(USERS_F, data)
                st.success("User added.")
                st.rerun()

    st.markdown("**Reset password / delete**")
    others = [u for u in users() if u["username"] != user["username"]]
    if others:
        pick = st.selectbox("User", others, format_func=lambda u: f"{u['username']} ({ROLES[u['role']]})")
        c1, c2 = st.columns(2)
        new_pw = c1.text_input("New password", type="password", key="rp")
        if c1.button("Reset password") and new_pw:
            change_password(pick["username"], new_pw)
            st.success("Password reset.")
        if c2.button("🗑️ Delete user"):
            with _lock:
                _write(USERS_F, [u for u in users() if u["username"] != pick["username"]])
            st.rerun()


def page_settings(user):
    st.subheader("⚙️ Settings")
    s = settings()
    with st.form("settings"):
        c1, c2 = st.columns(2)
        op = c1.time_input("Opening time", datetime.strptime(s["open_time"], "%H:%M").time(), step=1800)
        cl = c2.time_input("Closing time", datetime.strptime(s["close_time"], "%H:%M").time(), step=1800)
        adv = c1.number_input("Advance booking window (days)", 1, 30, int(s["advance_days"]))
        mx = c2.number_input("Max bookings per student per day", 1, 5, int(s["max_bookings_per_day"]))
        contact = st.text_input("Sports club contact (shown to students for disputes)", s["club_contact"])
        if st.form_submit_button("Save settings", type="primary"):
            if cl <= op:
                st.error("Closing time must be after opening time.")
            else:
                _write(SETTINGS_F, {"open_time": op.strftime("%H:%M"), "close_time": cl.strftime("%H:%M"),
                                    "advance_days": int(adv), "max_bookings_per_day": int(mx),
                                    "club_contact": contact})
                st.success("Saved.")
                st.rerun()


def page_account(user):
    st.subheader("🔑 Change password")
    with st.form("pw"):
        new = st.text_input("New password", type="password")
        new2 = st.text_input("Confirm new password", type="password")
        if st.form_submit_button("Update"):
            if len(new) < 6:
                st.error("Use at least 6 characters.")
            elif new != new2:
                st.error("Passwords don't match.")
            else:
                change_password(user["username"], new)
                st.success("Password updated.")


def page_dashboard(user):
    st.subheader("📊 Today's overview")
    today = now().strftime("%Y-%m-%d")
    bk = active_bookings(day=today)
    c1, c2, c3 = st.columns(3)
    c1.metric("Bookings today", len(bk))
    c2.metric("Total confirmed (all time)", len(active_bookings()))
    c3.metric("Registered students", len([u for u in users() if u["role"] == "student"]))
    st.dataframe(bookings_df(bk), use_container_width=True, hide_index=True)


# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------
def login_screen():
    st.title("🏟️ ICFAI Hyderabad — Sports Court Booking")
    st.caption("Volleyball • Basketball • Cricket • Tennis")
    tab_login, tab_reg = st.tabs(["Login", "Student registration"])
    with tab_login:
        with st.form("login"):
            u = st.text_input("Username / Roll number")
            p = st.text_input("Password", type="password")
            if st.form_submit_button("Login", type="primary"):
                user = authenticate(u, p)
                if user:
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        st.caption("Staff accounts are created by the administrator. Students: register in the next tab.")
    with tab_reg:
        with st.form("reg"):
            roll = st.text_input("Roll number (this will be your username)")
            name = st.text_input("Full name")
            p1 = st.text_input("Password (min 6 chars)", type="password")
            p2 = st.text_input("Confirm password", type="password")
            if st.form_submit_button("Register"):
                if not (roll.strip() and name.strip()):
                    st.error("Roll number and name are required.")
                elif len(p1) < 6:
                    st.error("Password must be at least 6 characters.")
                elif p1 != p2:
                    st.error("Passwords don't match.")
                else:
                    ok, msg = register_student(roll, name, p1)
                    (st.success if ok else st.error)(msg)


def main():
    init_storage()
    if "user" not in st.session_state:
        login_screen()
        return

    user = st.session_state.user
    role = user["role"]

    menus = {
        "student": {
            "📅 Availability": page_availability,
            "🏐 Book a court": page_book,
            "📋 My bookings": page_my_bookings,
            "🔑 Password": page_account,
        },
        "club_head": {
            "📊 Dashboard": page_dashboard,
            "🏆 Tournament blocks": page_closures,
            "📋 All bookings": page_all_bookings,
            "📅 Availability": page_availability,
            "🔑 Password": page_account,
        },
        "administrator": {
            "📊 Dashboard": page_dashboard,
            "📋 All bookings": page_all_bookings,
            "🏆 Tournament blocks": page_closures,
            "👥 Users": page_users,
            "⚙️ Settings": page_settings,
            "📅 Availability": page_availability,
            "🏐 Book a court": page_book,
            "🔑 Password": page_account,
        },
    }[role]

    with st.sidebar:
        st.markdown(f"### 👋 {user['name']}")
        st.caption(f"{ROLES[role]} • {user['username']}")
        choice = st.radio("Menu", list(menus), label_visibility="collapsed")
        st.divider()
        if st.button("Logout"):
            del st.session_state.user
            st.rerun()

    # Admin booking on behalf of themselves needs a 'student-like' identity: works as-is.
    menus[choice](user)


main()
