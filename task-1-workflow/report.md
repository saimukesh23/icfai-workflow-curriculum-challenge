# Task 1: Digital Sports Ground Booking Platform - Workflow Investigation and Proposal

**Institution:** ICFAI Foundation for Higher Education, Hyderabad  
**Investigator:** N. Sai Mukesh  
**Investigation period:** 21–24 October 2026  
**Report date:** 24 October 2026  
**Version:** 1.1

## 1. Executive Summary

This investigation examines how students at ICFAI Hyderabad currently access sports grounds for recreational activities, including football, basketball, volleyball and cricket.

Over the three days preceding this report, the investigator conducted informal conversations with 10 students and documented the findings in handwritten notes. All 10 students reported that there is no official ground-booking process. Students generally go to the ground and play if it is available. If other students are already playing, they either join the ongoing game or wait until it finishes.

The investigator subsequently discussed the proposed solution with a friend who heads the sports club. The sports-club head agreed that a digital booking platform would be helpful.

Based on these findings, this report proposes a digital sports ground booking platform through which students can check availability and book a ground for a maximum of one hour per booking. The platform would make scheduled use more predictable, reduce uncertainty about availability and provide a transparent way to coordinate access across multiple sports.

The proposal is intended to improve the current informal process, not to claim that students currently follow an official booking procedure. The platform would require appropriate coordination with the sports club before implementation.

## 2. Investigation Objective and Scope

### 2.1 Objective

To investigate the existing process through which students obtain access to sports grounds and propose a practical digital workflow for booking and coordinating ground usage.

### 2.2 Scope

The investigation covers:
- Informal access to sports grounds.
- How students determine whether a ground is available.
- What students do when a ground is already occupied.
- The absence of an official booking process, as reported by the interviewed students.
- A proposed digital booking workflow with a maximum booking duration of one hour.
- Coordination and oversight by the sports club.

The sports covered include football, basketball, volleyball, cricket and other activities that use campus sports grounds.

### 2.3 Investigation method

The investigator conducted informal conversations with 10 students over three days, from 21 to 24 October 2026, and recorded the findings in handwritten notes. The conversations focused on how students know whether a ground is available and what they do when other students are already playing.

After these conversations, the investigator discussed the proposed digital booking platform with a friend who heads the sports club. The sports-club head agreed that such a platform would be helpful.

This was an informal, exploratory investigation rather than a formal campus-wide survey or an audit of institutional records.

## 3. Current-State Workflow

### 3.1 Observed process

The current process is informal and based on students physically checking the ground.

1. A student or group decides to play a sport.
2. The students go to the relevant sports ground.
3. If the ground is available, they begin playing.
4. If other students are already playing, they either join the ongoing game or wait until it finishes.
5. Once the ground becomes available, the next group starts playing.

There is no official booking process according to all 10 students interviewed.

### 3.2 Current workflow diagram

```text
Student wants to play
        |
        v
Goes to the sports ground
        |
        v
Is the ground available?
        |
   +----+----+
   |         |
  Yes        No
   |         |
   |         v
   |   Join the ongoing game or wait until it finishes
   |         |
   |         v
   |   Ground becomes available
   |         |
   +----+----+
        |
        v
  Play the sport
```

### 3.3 Evidence summary

| Evidence ID | Evidence collected | Finding |
|---|---|---|
| E01 | Informal conversations with 10 students over three days | All 10 reported that there is no official booking process. |
| E02 | Student accounts of the existing access process | Students generally go to the ground and play if it is available. |
| E03 | Student accounts of occupied grounds | Students either join the ongoing game or wait until it finishes. |
| E04 | Discussion with a friend who heads the sports club | The sports-club head agreed that a digital booking platform would be helpful. |
| E05 | Investigator's proposed solution | An app allowing students to book a ground for a maximum of one hour per booking. |

The student conversations were recorded in handwritten notes. The findings above summarize the evidence collected; they are not fabricated direct quotations.

## 4. Problem Identification

The current process depends on students physically visiting a ground to determine whether they can play. Because there is no official booking process, students cannot rely on a centralized reservation record to see whether a particular ground or time slot has already been allocated.

This creates three potential workflow problems:

1. **Uncertain availability:** Students may not know whether a ground will be free when they arrive.
2. **Uncoordinated access:** Groups resolve occupancy informally by joining an ongoing game or waiting for it to finish.
3. **Lack of scheduled allocation:** Students do not have an official booking mechanism through which they can reserve a defined period in advance.

These findings establish an opportunity to improve coordination. The investigation did not measure average waiting time, the number of unsuccessful visits or the amount of time lost, so the scale of the impact has not been quantified.

## 5. Proposed Solution: Digital Sports Ground Booking Platform

### 5.1 Overview

Develop a digital application that enables students to view ground availability and reserve a ground for a maximum of one hour per booking.

The platform would introduce a structured scheduling process while preserving the existing informal process until the sports club approves and adopts the new system.

### 5.2 Proposed booking workflow

1. **Open the application:** A student accesses the sports ground booking platform.
2. **Select a sport and ground:** The student chooses the required sport and the corresponding available ground.
3. **View availability:** The application displays the ground's available and booked time slots.
4. **Select a time slot:** The student selects a suitable date and start time.
5. **Validate the request:** The application verifies that the requested slot is available and that the booking duration does not exceed one hour.
6. **Confirm the booking:** If the request passes validation, the application records the reservation and displays a confirmation.
7. **Use the ground:** The student or group uses the ground during the reserved period, subject to the rules established by the sports club.
8. **Release the slot:** After the booking ends or is cancelled, the slot becomes available according to the platform's rules.

This workflow is the proposed design; it is not a description of a system that has already been deployed.

### 5.3 Proposed workflow diagram

```text
Student opens the booking application
        |
        v
Selects the sport and ground
        |
        v
Views available and booked slots
(closures entered by the sports club are shown as unavailable)
        |
        v
Selects date and start time (maximum one hour)
        |
        v
Application validates the request:
 - slot is free (no overlapping confirmed booking)
 - duration is no longer than one hour
 - slot is not inside an authorized closure
        |
   +----+----------------+
   |                     |
  Valid               Not valid
   |                     |
   |                     v
   |        Application shows the reason
   |        and the student picks another slot
   |        (returns to "Selects date and start time")
   v
Booking confirmed and recorded
(date, ground, start time, end time, status)
        |
        +--------------------------+
        |                          |
        v                          v
Student uses the ground      Student cancels the booking
during the reserved hour     before it starts
        |                          |
        v                          v
Booking ends  ------>  Slot is released and shown as available

Sports club representative (separate path):
 - enters closures and updates ground availability
 - resolves disputes and exceptional cases
 - if the application is unavailable, follows the fallback procedure
   agreed with the sports club
```

### 5.4 Proposed booking rules

- Each booking may last for a maximum of one hour.
- A ground cannot have two overlapping confirmed bookings.
- Only available slots can be confirmed.
- The application should clearly display the date, ground, start time and end time for every booking.
- Students should be able to view their booking status and cancel a booking according to the rules established by the sports club.
- The platform should display any ground closures or restrictions entered by an authorized sports-club representative.
- The sports club should be able to manage ground availability and resolve disputes or exceptional cases.
- Booking limits, cancellation deadlines, repeat bookings and any priority rules should be finalized with the sports club before implementation.

### 5.5 Handling existing games and informal use

The proposed platform must account for the existing practice of students joining games or waiting for an occupied ground to become free.

Before launch, the sports club should establish how scheduled bookings interact with walk-up access. For example, it must decide whether a confirmed booking takes priority over an informal game and how students should handle a conflict between an ongoing game and the next scheduled slot.

The application should communicate these rules clearly. It should not automatically remove students from an ongoing game or claim that a ground is available unless the applicable scheduling rules support that status.

### 5.6 Sports-club coordination

The sports-club head's feedback supports the usefulness of exploring this proposal. Before implementation, the sports club should confirm the booking policy, authorized administrators, ground list, slot schedule, exception handling and process for handling disputes.

The sports club would be the proposed operational stakeholder responsible for coordinating the platform with actual ground usage.

## 6. Functional Requirements

| ID | Requirement | Purpose |
|---|---|---|
| FR01 | Display the available sports grounds | Allows students to identify suitable grounds |
| FR02 | Display available and booked time slots | Reduces uncertainty about scheduled use |
| FR03 | Allow students to select a sport, ground, date and time | Captures the intended booking |
| FR04 | Enforce a maximum booking duration of one hour | Implements the proposed booking limit |
| FR05 | Prevent overlapping confirmed bookings for the same ground | Avoids conflicting reservations |
| FR06 | Provide booking confirmation and status | Gives students a clear record of their reservation |
| FR07 | Allow cancellation under the approved cancellation rules | Enables unused slots to be released |
| FR08 | Allow authorized sports-club representatives to update availability | Keeps the schedule aligned with approved restrictions |
| FR09 | Display official ground closures and relevant restrictions | Prevents booking during unavailable periods |
| FR10 | Maintain a record of booking and schedule changes | Supports accountability and dispute resolution |

These are proposed functional requirements. They should be validated with the sports club before development.

## 7. Acceptance Tests

The following tests define expected behaviour for a future prototype. They are test cases, not claims of completed execution.

| Test ID | Scenario | Expected result |
|---|---|---|
| T01 | Student requests an available 60-minute slot | The application accepts the request if all other rules are satisfied and confirms the booking. |
| T02 | Student requests a slot longer than 60 minutes | The application rejects the duration or asks the student to choose a valid slot no longer than one hour. |
| T03 | Two students request overlapping times on the same ground | The application prevents both requests from becoming confirmed for the same overlapping period. |
| T04 | Student attempts to book a ground during an authorized closure | The application prevents the booking and displays the ground's unavailable status. |
| T05 | A student cancels a confirmed booking | The application records the cancellation and releases the slot according to the approved policy. |

Before deployment, each test should be run against the implemented application and its actual result recorded. No test is reported as passed in this investigation.

## 8. Expected Benefits and Evaluation Plan

### 8.1 Expected benefits

The proposed platform is intended to:
- Make scheduled ground availability easier to check.
- Allow students to plan sports activities before arriving.
- Reduce conflicts caused by overlapping reservations.
- Provide a clear one-hour maximum booking period.
- Improve coordination between students and the sports club.
- Create a record of reservations, cancellations and authorized closures.

These are expected benefits, not measured outcomes.

### 8.2 Evaluation metrics

A pilot should measure:
- Number of bookings made per week.
- Percentage of bookings successfully completed.
- Number of overlapping booking attempts prevented.
- Number of students who arrive and find that a confirmed slot cannot be used.
- Number of cancellations and unused bookings.
- Student feedback on ease of use.
- Administrative effort required to maintain the schedule.

Waiting time and unsuccessful visits should be recorded before and during a pilot if the sports club wants to determine whether the application reduces them.

### 8.3 Cost-effectiveness

The initial implementation should prioritize core features: ground selection, availability display, one-hour booking validation, conflict prevention and confirmation.

The platform's value should be assessed against the cost of development, hosting, maintenance and sports-club administration. No monetary savings or return on investment are claimed because no cost or baseline performance data were collected during this investigation.

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Students continue using the informal process | Explain the booking rules and introduce the platform through the sports club |
| Students arrive for an ongoing game despite having a booking | Define and communicate the policy for conflicts between bookings and ongoing games |
| Two students attempt to book the same slot | Validate availability when confirming the booking |
| Schedule information is outdated | Restrict schedule updates to authorized representatives and record the last update |
| Students make bookings they do not use | Establish reasonable cancellation and no-show rules with the sports club |
| Demand exceeds the number of available slots | Use transparent allocation rules and review usage data |
| Technical failure prevents access to booking information | Establish a fallback procedure through the sports club |
| Administrative effort becomes excessive | Start with a limited pilot and evaluate maintenance effort before expanding |

## 10. Limitations

The investigation involved informal conversations with 10 students over three days and one discussion with a friend who heads the sports club. The student findings were recorded in handwritten notes.

The investigation did not include a formal campus-wide survey, measured waiting times, booking-system usage statistics, a cost analysis, a deployed application or executed software tests.

The evidence supports the conclusion that the interviewed students described ground access as informal and that the sports-club head considered a digital booking platform helpful. It does not establish that every student experiences the same problems or that the proposed application will necessarily reduce waiting time.

The proposed booking workflow, one-hour limit and functional requirements are design recommendations that require operational agreement with the sports club.

## 11. Conclusion

The investigation found that all 10 students interviewed described a walk-up process rather than an official ground-booking system. Students generally go to the ground and play if it is available; if others are playing, they either join them or wait until the game finishes. The sports-club head agreed that a digital booking platform would be helpful.

The recommended next step is to develop and evaluate a small prototype that displays ground availability, allows bookings of up to one hour, prevents overlapping confirmed reservations and communicates booking status clearly.

The sports club should validate the allocation rules and the relationship between scheduled bookings and existing walk-up play before a pilot begins. The pilot should then measure actual usage, booking conflicts, student feedback and administrative effort to determine whether the platform improves ground access.

## Appendix: Supporting Evidence

The investigation is supported by:
- Handwritten notes from conversations with 10 students conducted over the three-day investigation period.
- Notes from the discussion with the sports-club head.
- The proposed workflow and acceptance-test plan documented in this report.

No individual student names or fabricated quotations are included.
