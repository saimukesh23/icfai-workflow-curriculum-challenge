# Task 1: Digital Sports Ground Booking Platform — Workflow Investigation, Proposal and MVP

**Institution:** ICFAI Foundation for Higher Education, Hyderabad  
**Investigator:** N. Sai Mukesh  
**Investigation period:** 21–24 October 2026  
**Report date:** 24 October 2026  
**Version:** 2.1  
**Status:** Investigation completed; MVP deployed; feature verification and testing in progress

**Live MVP:** https://ground-booking.streamlit.app/

---

## 1. Executive Summary

This investigation examines how students at ICFAI Hyderabad currently access sports grounds for recreational activities, including football, basketball, volleyball and cricket.

Over three days, the investigator conducted informal conversations with 10 students and documented the findings in handwritten notes. All 10 students reported that there is no official ground-booking process. Students generally visit the ground and play if it is available. If other students are already playing, they either join the ongoing game or wait until it finishes.

The investigator also discussed the proposed solution with a friend who heads the sports club. The sports-club head agreed that a digital booking platform would be helpful. This informal feedback supports further exploration but does not constitute formal institutional approval.

Based on these findings, the investigator developed a digital sports ground booking MVP and deployed it on Streamlit.

**Live application:** https://ground-booking.streamlit.app/

The intended workflow allows students to view ground availability and reserve a suitable time slot. The current booking-duration requirement is a minimum of 30 minutes and a maximum of 60 minutes. The deployed application must be tested to confirm that these limits and the other intended booking constraints are enforced correctly.

This report distinguishes the original investigation findings, proposed operating policies, the current MVP and functionality that still requires verification. The accompanying `testcase.csv` records the designed test scenarios and their verification status.

The next step is to verify the deployed application's behaviour, document incomplete functionality, resolve defects and evaluate whether the MVP is suitable for a limited pilot. No improvement in waiting time, booking conflicts or administrative effort is claimed without measured evidence.

## 2. Investigation Objective and Scope

### 2.1 Objective

To investigate the existing process through which students obtain access to sports grounds and propose a practical digital workflow for booking and coordinating ground usage.

### 2.2 Scope

The investigation and proposal cover:

- The existing informal process for accessing sports grounds.
- How students determine whether a ground is available.
- What students do when a ground is occupied.
- The absence of an official booking process, as reported by the interviewed students.
- A digital booking workflow with a minimum duration of 30 minutes and a maximum duration of 60 minutes.
- Sports-club coordination, tournament closures and dispute handling.
- Functional requirements, test scenarios and an evaluation plan.
- Development and deployment of an MVP, with further feature verification in progress.

The sports covered include football, basketball, volleyball, cricket and other activities that use campus sports grounds.

### 2.3 Investigation Method

The investigator conducted informal conversations with 10 students over three days, between 21 and 24 October 2026, and recorded the findings in handwritten notes. The conversations focused on how students know whether a ground is available and what they do when other students are already playing.

After these conversations, the investigator discussed the proposed digital booking platform with a friend who heads the sports club. The sports-club head agreed that such a platform would be helpful.

This was an informal, exploratory investigation rather than a formal campus-wide survey or an audit of institutional records. Individual conversation timestamps and verbatim quotations are not presented because they are not required to substantiate the aggregate findings.

## 3. Current-State Workflow

### 3.1 Observed Process

The current process is informal and based on students physically checking the ground.

1. A student or group decides to play a sport.
2. The students go to the relevant sports ground.
3. If the ground is available, they begin playing.
4. If other students are already playing, they either join the ongoing game or wait until it finishes.
5. Once the ground becomes available, the next group starts playing.

According to all 10 students interviewed, there is no official booking process.

### 3.2 Current Workflow Diagram

```text
Student wants to play
        |
        v
Goes to the sports ground
        |
        v
Is the ground available?
        |
    +---+---+
    |       |
   Yes      No
    |       |
    |       v
    |   Join the ongoing game
    |   or wait until it finishes
    |       |
    |       v
    |   Ground becomes available
    |       |
    +---+---+
        |
        v
   Play the sport
```

### 3.3 Evidence Summary

| Evidence ID | Evidence collected | Finding |
|---|---|---|
| E01 | Informal conversations with 10 students over three days | All 10 reported that there is no official booking process. |
| E02 | Student accounts of the existing access process | Students generally go to the ground and play if it is available. |
| E03 | Student accounts of occupied grounds | Students either join the ongoing game or wait until it finishes. |
| E04 | Discussion with a friend who heads the sports club | The sports-club head agreed that a digital booking platform would be helpful. |
| E05 | Investigator's proposed solution | An application allowing students to book a ground for 30–60 minutes. |

The student conversations were recorded in handwritten notes. E01–E03 summarize aggregate findings from those conversations; they should not be interpreted as three separate sets of interviews. E05 is a proposed solution, not an observed finding.

### 3.4 Evidence Limitations

The investigation did not measure average waiting time, the number of unsuccessful visits, booking demand by sport or the frequency of disputes. It also did not include a formal campus-wide survey.

Consequently, the findings establish the reported process among the interviewed students but do not establish how frequently availability problems occur across the entire campus.

## 4. Problem Identification

The current process depends on students physically visiting a ground to determine whether they can play. Since the interviewed students reported no official booking process, students cannot rely on a centralized reservation record to determine whether a particular ground or time slot has been allocated.

Three potential workflow problems emerge:

1. **Uncertain availability:** Students may not know whether a ground will be free when they arrive.
2. **Uncoordinated access:** Groups resolve occupancy informally by joining an ongoing game or waiting for it to finish.
3. **Lack of scheduled allocation:** Students do not have an official mechanism for reserving a defined period in advance.

A digital booking platform could provide a shared schedule and make reservations visible to students and authorized sports-club representatives.

However, software alone cannot resolve every access issue. The sports club must agree on how confirmed reservations interact with ongoing games, tournament closures and students who arrive without a booking.

## 5. Solution Design and Implemented MVP

### 5.1 Overview

The proposed digital sports ground booking platform is intended to allow students to:

- View sports grounds and their availability.
- Select a sport, ground, date and time.
- Reserve an available slot for a duration of 30–60 minutes.
- Receive a booking confirmation.
- Review or cancel reservations according to the approved policy.
- Access the designated sports-club contact for complaints or booking disputes.

The sports-club team would maintain the schedule, coordinate tournament closures and resolve operational exceptions.

### 5.2 Current MVP and Deployment

A web-based MVP has been developed and deployed using Streamlit Community Cloud.

- **Live application:** https://ground-booking.streamlit.app/
- **Main application file:** `Task-1/app.py`
- **Dependency file:** `Task-1/requirements.txt`
- **Test-case register:** `Task-1/testcase.csv`

The MVP demonstrates the current implementation of the booking workflow. Its deployment establishes that a hosted application has been published, but deployment alone does not establish that every functional requirement works correctly.

Feature-level verification should be conducted against the test scenarios in `testcase.csv`. The results should distinguish tests that have passed, tests that have failed, tests that have not yet been run and requirements awaiting stakeholder approval.

The application is described as an MVP rather than a production-ready campus booking system. Any functionality that is incomplete, untested or dependent on an unresolved sports-club policy must be identified explicitly.

### 5.3 Intended Booking Workflow

1. **Open the application:** A student accesses the sports ground booking platform.
2. **Select a sport and ground:** The student chooses the required sport and corresponding ground.
3. **View availability:** The application displays available slots, confirmed bookings and authorized closures, where implemented.
4. **Select a time slot:** The student selects a date and start time.
5. **Validate the request:** The application should check that the required details are present, the duration is within 30–60 minutes, the slot is available and no authorized closure applies.
6. **Confirm the booking:** If validation succeeds, the application records the reservation and displays confirmation.
7. **Use the ground:** The student or group uses the ground during the reserved period, subject to the policy approved by the sports club.
8. **Complete or cancel:** At the end of the reservation, or after an eligible cancellation, the slot becomes available according to the platform's rules.

This describes the intended workflow. Each step must be verified against the deployed application before it is reported as implemented and working.

### 5.4 Proposed Workflow Diagram

```text
Student opens the booking application
                 |
                 v
       Selects sport and ground
                 |
                 v
        Views ground availability
                 |
                 v
       Selects date and start time
       (duration: 30–60 minutes)
                 |
                 v
       Application validates request
       - Required details are present
       - Duration is within permitted limits
       - Slot is available
       - No overlapping booking exists
       - No authorized closure applies
                 |
           +-----+-----+
           |           |
         Valid       Invalid
           |           |
           v           v
   Booking confirmed  Show error and
   and recorded       request correction
           |           |
           |           +----> Select another
           |                  slot or correct
           |                  the request
           v
     Student uses ground
           |
           v
 Booking ends or is cancelled
           |
           v
     Slot is released

Separate sports-club workflow:
- Maintain ground schedules
- Close slots during tournaments
- Update authorized restrictions
- Handle complaints and disputes
- Coordinate fallback arrangements
  if the application is unavailable
```

### 5.5 Proposed Booking and Access Rules

The following rules require approval before the application is used as an official campus booking system.

1. **Duration:** Each booking must last at least 30 minutes and no longer than 60 minutes.
2. **No overlapping reservations:** The same ground cannot have two overlapping confirmed bookings.
3. **Required details:** A booking must contain the student identifier or approved account, sport, ground, date, start time and end time.
4. **Confirmation:** A reservation is considered confirmed only after the system successfully records it.
5. **Cancellation:** Students may cancel according to the policy approved by the sports club.
6. **Schedule administration:** Only authorized sports-club representatives may create official closures or modify ground availability.
7. **Tournament closures:** The sports-club team must be informed of tournaments in advance and must close affected grounds or slots in the application for the relevant period.
8. **Disputes:** The application should provide the sports-club president's contact number, subject to permission to publish it, so students can call or WhatsApp with their booking confirmation as supporting evidence.
9. **System failure:** If the application is unavailable, students should follow a fallback procedure agreed upon with the sports club rather than relying on an unverified booking status.
10. **Policy approval:** Cancellation deadlines, repeat bookings, no-show handling and priority rules must be finalized with the sports club.

### 5.6 Handling Existing Games and Walk-Up Access

The proposed application must account for the existing practice of students joining games or waiting for an occupied ground to become free.

The proposed access policy is:

- Students should check the application before using a ground.
- A student with a valid confirmed booking should be able to show the booking confirmation when arriving for the reserved slot.
- If another group is using the ground during a valid reserved slot, the proposed policy is for the group currently using the ground to leave so the booking holder can use the reserved time.
- Complaints or disagreements should be referred to the sports club, with the booking confirmation used as supporting evidence.
- Students should not be expected to resolve serious disputes themselves.

This policy changes the current informal arrangement and therefore requires explicit approval and communication by the sports club before launch. The application cannot enforce this rule physically; operational coordination is still necessary.

### 5.7 Sports-Club Responsibilities

The sports club would be the proposed operational owner of the platform.

Its responsibilities would include:

- Maintaining the list of bookable grounds and approved time slots.
- Reviewing tournament schedules and closing affected slots in advance.
- Keeping availability information accurate.
- Authorizing representatives who can change the schedule.
- Handling complaints and booking conflicts.
- Communicating the booking and walk-up access policies.
- Maintaining a fallback process for technical failures.
- Reviewing pilot results and deciding whether the platform should continue or change.

The sports-club head's feedback supports exploring the proposal. It does not, by itself, constitute formal institutional approval or confirmation that the sports club has accepted these responsibilities.

## 6. Functional Requirements

| ID | Requirement | Purpose |
|---|---|---|
| FR01 | Display available sports grounds | Helps students identify suitable grounds. |
| FR02 | Display available, booked and closed time slots | Reduces uncertainty about scheduled use. |
| FR03 | Allow selection of sport, ground, date and time | Captures the intended booking. |
| FR04 | Enforce a minimum duration of 30 minutes and a maximum duration of 60 minutes | Implements the updated booking-duration rule. |
| FR05 | Prevent overlapping confirmed bookings for the same ground | Avoids conflicting reservations. |
| FR06 | Provide booking confirmation and status | Gives students a clear record of their reservation. |
| FR07 | Allow cancellation under the approved policy | Enables unused slots to be released. |
| FR08 | Allow authorized representatives to update availability | Keeps the schedule aligned with approved restrictions. |
| FR09 | Display tournament closures and other official restrictions | Prevents booking during unavailable periods. |
| FR10 | Maintain a record of bookings, cancellations and schedule changes | Supports accountability and dispute resolution. |
| FR11 | Display an approved sports-club contact method | Provides an escalation route for complaints. |
| FR12 | Handle failed submissions without falsely confirming a booking | Reduces uncertainty and duplicate submissions. |

These are proposed functional requirements. They must be compared against the current implementation and validated with the sports club before the application is used operationally.

## 7. Test Cases and Acceptance Criteria

### 7.1 Test-Case Register

The file `Task-1/testcase.csv` records the test scenarios, preconditions, test actions, expected results, recovery steps, decision responsibilities and status.

The scenarios include:

- Normal booking requests.
- Missing required information.
- Duplicate or overlapping booking attempts.
- Unauthorized requests.
- Booking submission failures.
- Requests below the 30-minute minimum.
- Requests exceeding the 60-minute maximum.

These are designed test scenarios. A defined test case is not evidence that the deployed application has passed it.

### 7.2 Acceptance Criteria

The MVP should meet the following criteria before a pilot:

- A valid request for an available slot lasting between 30 and 60 minutes can be recorded and confirmed.
- Requests shorter than 30 minutes are rejected.
- Requests longer than 60 minutes are rejected.
- Missing required details produce a clear validation message.
- Conflicting confirmed bookings cannot be created for the same ground and time.
- Students cannot create official closures or change administrative schedules without authorization, if schedule administration is supported.
- Slots closed for tournaments cannot be booked, if tournament closures are implemented.
- A failed submission does not result in an incorrect confirmation or unintended duplicate.
- Booking status can be checked and a cancellation is reflected in the schedule, if these features are implemented.
- The approved sports-club contact and fallback instructions are available to students before an official launch.

Each test must be run against the implemented application, with the actual result recorded as pass or fail. Tests that have not been executed must remain pending. Requirements that are not implemented must be documented as incomplete rather than passed.

### 7.3 Test Status Definitions

| Status | Meaning |
|---|---|
| Passed | The test was executed and the observed result matched the expected result. |
| Failed | The test was executed and the observed result did not match the expected result. |
| Pending verification | The test has not yet been executed or its outcome has not been documented. |
| Blocked | The test cannot be completed because a dependency, policy or feature is unavailable. |
| Awaiting policy approval | The expected behaviour depends on a rule that has not been formally approved. |

The test-case register should use these meanings consistently.

## 8. Expected Benefits and Evaluation Plan

### 8.1 Expected Benefits

The proposed platform is intended to:

- Make scheduled ground availability easier to check.
- Allow students to plan sports activities before arriving.
- Reduce uncertainty about whether a ground is reserved.
- Prevent conflicting reservations through validation.
- Enforce a booking-duration range of 30–60 minutes.
- Improve coordination between students and the sports club.
- Provide a record that can support complaint resolution.
- Make tournament-related closures visible in the schedule.

These are expected benefits, not measured outcomes.

### 8.2 Evaluation Metrics

A limited pilot should track:

- Number of bookings made per week.
- Percentage of bookings successfully completed.
- Number of overlapping booking attempts prevented.
- Number of students who arrive and cannot use a confirmed slot.
- Number of cancellations and unused bookings.
- Student feedback on ease of use.
- Number of booking complaints and time required to resolve them.
- Administrative effort required to maintain schedules and closures.
- Application failures and booking-status discrepancies.

Waiting time and unsuccessful visits should be recorded before and during the pilot if the sports club wants to determine whether the application reduces them.

### 8.3 Net Time-Saving Estimate

Net time savings should include not only the time saved by students or staff but also the additional time needed to operate the application.

**Formula:**

Net time saved per month = Baseline monthly effort − Post-implementation monthly effort

Post-implementation effort should include schedule maintenance, booking administration, cancellations, support, complaint handling and technical maintenance where applicable.

**Illustrative example only — not measured campus data:**

| Activity | Monthly effort |
|---|---:|
| Estimated effort under the existing process | 300 minutes |
| Estimated effort after introducing the platform, including administration and support | 180 minutes |
| Illustrative net time saved | 120 minutes per month |

The figures above are hypothetical values used to demonstrate the calculation. They are not estimates derived from the 10 student conversations and must not be presented as actual savings.

The pilot should collect real baseline and post-implementation data before making a claim about time saved. Development effort and implementation costs should also be evaluated separately.

### 8.4 Cost-Effectiveness

The initial implementation should prioritize core functionality: ground selection, availability display, duration validation, conflict prevention, confirmation, schedule administration and complaint escalation.

The platform's value should be assessed against development, hosting, maintenance and administrative costs. A simple application using standard scheduling rules and database constraints may be sufficient for the initial use case.

No monetary savings, return on investment or measured efficiency improvement is claimed because no baseline performance or cost data were collected.

### 8.5 Role of AI in This Proposal

AI was used as an assistance tool for brainstorming, organizing the proposal and structuring the report. The investigation findings themselves are based on the reported student conversations and the discussion with the sports-club head, not on AI-generated evidence.

AI is not necessary for the core booking workflow. Ground selection, duration validation, availability checks, authorization, conflict prevention and booking confirmation can be implemented through ordinary application logic and database constraints.

Adding AI to the booking process would introduce complexity without a demonstrated need. An optional future feature, such as a question-answering assistant for booking rules, could be considered only if user feedback shows that it would provide value.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Students continue using the informal process | Explain the booking rules and introduce the platform through the sports club. |
| A student arrives while another group is using the ground | Establish and communicate the approved policy for conflicts between confirmed bookings and ongoing games. |
| Two students attempt to book the same slot | Check availability when confirming a booking and enforce conflict prevention in the database. |
| Schedule information is outdated | Restrict schedule updates to authorized representatives and retain a record of changes. |
| Tournament closures are not entered in time | Establish an advance notification process between tournament organizers and the sports-club team. |
| Students make bookings they do not use | Establish reasonable cancellation and no-show rules with the sports club. |
| Unauthorized users modify official schedules | Apply authentication and role-based access control where administrative features are implemented. |
| A booking conflict becomes a dispute | Provide the approved sports-club contact and a process for checking booking confirmation. |
| Technical failure prevents access to booking information | Establish a fallback procedure and avoid treating an unverified request as confirmed. |
| Administrative effort becomes excessive | Start with a limited pilot and compare the additional effort with the measured benefits. |
| Students are unaware of the new rules | Communicate the policy clearly before launch and display it in the application. |

## 10. Limitations and Conditions for Reconsideration

### 10.1 Investigation Limitations

The investigation involved informal conversations with 10 students over three days and one discussion with a friend who heads the sports club. Student findings were recorded in handwritten notes.

The investigation did not include:

- A formal campus-wide survey.
- Measured waiting times or unsuccessful visits.
- Booking-demand statistics by sport or ground.
- A detailed cost analysis.
- Formal institutional approval of the proposed access rules.
- Evidence that the proposed policy has been adopted by the sports club.

The evidence supports the conclusion that the interviewed students described ground access as informal and that the sports-club head considered a digital booking platform helpful. It does not establish that every student experiences the same problems or that the application will necessarily reduce waiting time.

### 10.2 MVP and Testing Limitations

The application is deployed, but its deployment does not establish that every intended feature works correctly.

The following limitations must be recorded according to the actual state of the implementation and testing:

- Features that are implemented but have not been tested.
- Features that are partially implemented or incomplete.
- Tests that have not been executed.
- Defects discovered during testing.
- Booking and access policies awaiting sports-club approval.
- Any limits affecting persistence, concurrency, authentication, administration or recovery from technical failures, if applicable to the implementation.

These items should be confirmed by inspecting the application and executing the test cases. This report does not claim that every listed functional requirement is implemented or passed.

### 10.3 When Should the Proposal Be Changed or Abandoned?

The proposal should be reviewed after consultation or a pilot if any of the following conditions occur:

1. Students rarely experience availability conflicts, making a booking system unnecessary.
2. The existing walk-up process is considered adequate by students and the sports club.
3. The sports club cannot agree on how confirmed bookings interact with ongoing games.
4. Tournament schedules and ground availability cannot be maintained accurately.
5. Student adoption is too low for the application to provide reliable scheduling information.
6. The time spent administering the platform exceeds the time and effort saved.
7. The number of disputes or failed bookings increases after introduction.
8. Development, hosting and maintenance costs are disproportionate to the demonstrated benefits.

Possible responses include simplifying the workflow, changing booking policies, running a smaller pilot or discontinuing the application if the evidence does not justify it.

## 11. Conclusion and Recommended Next Steps

The investigation found that all 10 students interviewed described a walk-up process rather than an official ground-booking system. Students generally go to the ground and play if it is available; if others are playing, they either join them or wait until the game finishes. The sports-club head agreed that a digital booking platform would be helpful.

A digital sports ground booking MVP has been developed and deployed on Streamlit. The intended platform allows students to view availability, book a ground for 30–60 minutes, receive confirmation and refer disputes to the sports club. The sports-club team would coordinate availability and close affected slots during tournaments.

The next steps are:

1. Verify that the deployed Streamlit application loads and supports its currently implemented workflow.
2. Execute the test scenarios in `testcase.csv` and record the actual results.
3. Test the 30-minute minimum and 60-minute maximum booking-duration boundaries.
4. Test missing information, overlapping booking attempts and submission failures where the relevant features are implemented.
5. Fix identified defects and document incomplete functionality.
6. Obtain the sports club's approval for booking priority, walk-up access, tournament closures, cancellations and dispute handling.
7. Conduct a limited pilot only if the relevant stakeholders approve it.
8. Measure usage, conflicts, administrative effort and student feedback before claiming that the platform improves the existing process.
9. Continue, modify or discontinue the system based on the results.

The proposal should be considered successful only if a pilot demonstrates practical value and the sports club can maintain the schedule and access rules reliably.

---

## Appendix A: Supporting Evidence

The investigation is supported by:

- Handwritten notes from conversations with 10 students conducted during the investigation period.
- Notes from the discussion with the sports-club head.
- The current-state workflow documented in this report.
- The proposed booking workflow and functional requirements.
- The deployed MVP at https://ground-booking.streamlit.app/
- The application's source file, `Task-1/app.py`.
- The dependency file, `Task-1/requirements.txt`.
- The test-case register, `Task-1/testcase.csv`.

No individual student names or fabricated quotations are included. The evidence summary records aggregate findings rather than attributing unsupported statements to specific students.

Application screenshots, test outputs and deployment logs should be added only when they have actually been captured. The deployed URL should be tested from a normal browser session before the final submission.

## Appendix B: Items Requiring Confirmation Before Official Implementation

| Item | Required confirmation |
|---|---|
| Ground inventory | Which grounds and sports can be booked? |
| Booking schedule | Which days and times are available for recreational use? |
| Booking duration | Is the 30–60 minute duration range approved? |
| Booking priority | Must a group using a ground leave when a valid booking holder arrives? |
| Tournament handling | Who informs the sports club, and how far in advance must closures be entered? |
| Administrative access | Which sports-club representatives can update the schedule? |
| Complaints | May the sports-club president's contact number be published in the application? |
| Cancellations and no-shows | What rules apply to unused bookings and late cancellations? |
| Technical failure | What fallback process should students follow if the application is unavailable? |
| Pilot approval | Who authorizes the pilot, and how will its results be evaluated? |

These items are unresolved implementation decisions, not facts established by the investigation.

## Appendix C: Individual Contribution and AI Use

The investigator conducted the informal student conversations, recorded the aggregate findings, discussed the proposed solution with a friend who heads the sports club, designed the booking workflow and requirements, developed the MVP, deployed it on Streamlit and prepared the supporting report and test-case register.

AI tools were used as assistance for brainstorming, drafting, structuring and reviewing parts of the proposal. AI assistance is not treated as evidence of student interviews, stakeholder approval, application functionality or executed tests.

Any AI-generated suggestions incorporated into the report should be reviewed by the investigator. Application behaviour should be verified by executing the relevant test cases, and unresolved policy decisions should be confirmed with the sports club before an official pilot.

The investigator remains responsible for the accuracy of the report, the implementation claims and the evidence submitted.
