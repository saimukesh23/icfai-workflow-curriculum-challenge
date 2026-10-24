# Task 2 — Curriculum Audit and Redesign Proposal

**Programme:** B.Tech CSE (AI & ML), ICFAI Tech, IFHE Hyderabad  
**Prepared:** 24 October 2026 · **Status:** Student proposal, not an approved university revision

## Executive summary
This report compares a student-provided 166-credit working map with three job descriptions and proposes a credit-neutral redesign for 2030 readiness. It improves practical assessment in selected programming, data, ML, GenAI and cloud courses; reallocates two credits toward Deep Learning and Computer Vision by conditionally reducing two other courses; replaces an existing 3-credit discipline-elective slot with Document Intelligence and Information Retrieval; and uses the existing 3-credit SP301 Special Project for the Task 1 sports-ground booking platform.

**Critical source-status note:** The public IFHE programme-structure page reviewed on 24 October 2026 differs materially from the supplied map in course codes, titles, semester placement and some credit values. This report therefore calls it a *student-provided working baseline*, not the authenticated official curriculum for a particular admission batch. Obtain the applicable batch regulation from the department/Registrar before formal submission. See `references.md`.

## 1. Current curriculum and gaps
The working map already lists foundations relevant to these roles: Computer Programming (CS101), Data Structures (CS102), OOP (CS201), DBMS (CS206), Algorithms (CS203), Operating Systems (CS302), Web Enabled Technologies (CS205), Python/R coding practice (DS202), Data Science (DS203), Machine Learning (DS304), Big Data Systems (DS307), Deep Learning (DS306), Generative AI (DS408) and Cloud Computing (CS307).

The defensible gap is not that these subjects are absent. Rather, practical depth is not established by course titles alone, and explicit OCR pipelines, hybrid retrieval evaluation, grounded answer verification, agent orchestration, production observability and failure recovery are not visible in the working course titles. Detailed syllabus and assessment inspection is needed before declaring any topic absent.

## 2. Job comparison
- **Document intelligence / AI-ML trainee — WINIT, Hyderabad; listing surfaced 17 Aug 2026.** Requirements include Python, SQL, LLM/RAG, document extraction/OCR and APIs/cloud. Existing programming, DBMS, ML, GenAI and cloud foundations are relevant; an explicit OCR/document-intelligence pipeline is not visible in course titles. Proposed response: elective replacement plus extraction/retrieval evaluation.
- **Full-Stack Software Engineer (Early Careers) — SuperApp; accessed 24 Oct 2026, posting date not displayed.** Requirements include end-to-end frontend/backend, APIs/data models, tests, AI workflow review, reliability/security/observability. Foundations are present; integrated production-style practice needs explicit assessment.
- **Junior AI/ML Engineer — DXC Luxoft, Hyderabad; listing surfaced 21 Oct 2026.** Requirements include Python, SQL, Git, RAG, embeddings/vector databases, LLM evaluation, agents and APIs. Existing ML/GenAI foundations are relevant; retrieval evaluation and agent safeguards need explicit practice.

These three listings are illustrative evidence, not a representative labour-market study. Full mapping is in `job-analysis.csv`.

## 3. Credit-balanced proposal
|Course|Current|Proposed|Delta|
|---|---:|---:|---:|
|MT101 Digital Fabrication|3|2|-1|
|DS306 Deep Learning|3|4|+1|
|CS305 Computer Vision|3|4|+1|
|MG401 Introduction to Entrepreneurship|3|2|-1|
|**Net**|||**0**|

Reductions are conditional on faculty review; they do not imply these subjects lack value. Proposed total remains 166 credits, subject to authentication of the batch baseline and summer-term accounting. Replace `DSXXX Discipline Elective-I` in Semester V with a proposed 3-credit Document Intelligence and Information Retrieval elective; this is a slot replacement, not an added course. The Semester VIII internship/research and thesis/seminar pathways are alternatives.

Assessment/learning changes affect 40 course credits across 11 existing courses, approximately **24.1% of 166**. This means 40 credits' worth of courses receive materially revised practical activities/assessment; it does not mean 40 credits are added or reallocated. Course list: CS101, CS102, CS206, CS205, DS202, DS304, DS305, DS306, DS307, DS408 and CS307.

## 4. Task 1 project inside SP301
Use the existing **SP301 Special Project**, Semester VI, 3 credits. No new course or additional credits.

Build a sports-ground booking platform with one-hour slots, availability browsing, prevention of overlapping confirmed bookings, and operator-controlled closures for approved tournaments. Use synthetic data unless real campus use is authorised. Restrict closures to an operator role and log actor, timestamp, slot and reason. Test duplicate submissions, concurrent booking attempts, API/database failure, interrupted confirmation, retries and unauthorised actions. Use an atomic database conflict check rather than relying on client-side availability.

**Acceptance tests:** overlapping requests cannot both confirm; closed slots cannot be booked; unauthorised users cannot close slots; retries do not duplicate bookings; failures show safe states; operator actions are auditable. Measure scripted conflict-test pass rate, acceptance-test pass rate, recovery time under simulated failure and usability-task completion time. Do not claim campus-wide impact without evidence.

## 5. AI-assisted exercises
`ai-exercises.md` records five exercises: stack-based balanced brackets (CS102); SQL repeat confirmed bookings (CS206); classification metrics (DS304); leakage-safe deep-learning workflow (DS306); and source-grounded booking-policy answer (DS408). It includes model/date, prompts, output summaries, manual verification and remaining human checks. No external code/SQL execution, model training or deployed RAG test is claimed. A key correction: repeat confirmed bookings are not the same as time-slot conflicts.

## 6. Stakeholder feedback and falsifiability
The author reports that an anonymised senior student agreed with the proposal overall. The date and verbatim comments were not recorded. This is informal student-level feedback, not faculty approval or evidence of improved outcomes.

The strongest claim is that practical assessment changes and targeted credit reallocation can improve role readiness without increasing total credits. It could be weakened or disproved if syllabus review shows these skills are already assessed adequately; employers say the gaps are not important; a pilot shows no improvement on common rubrics; or faculty/regulatory review shows credit reductions weaken essential outcomes or are infeasible.

## 7. Approval gates
1. Authenticate the admission-batch curriculum and reconcile codes, elective rules and summer internship accounting.
2. Obtain faculty review of the proposed credit changes, learning outcomes, contact hours and lab feasibility.
3. Approve the elective only as a replacement for an eligible existing slot.
4. Pilot SP301 using synthetic data and documented acceptance tests.
5. Compare practical outcomes against a defined baseline before claiming impact.

## Appendices
- **A — Full course map:** `course-map.md` and `course-map.csv`
- **B — Credit arithmetic:** baseline 166; target 20–25% = 33.2–41.5; affected-course scope 40/166 = 24.1%; credit deltas -1,+1,+1,-1 = net zero; elective replacement and SP301 add no credits.
- **C — Job evidence:** `job-analysis.csv` and `references.md`
- **D — Five AI exercises:** `ai-exercises.md`
- **E — Redesign and SP301 project design:** `redesign.md`
- **F — Stakeholder validation:** `validation.md`
