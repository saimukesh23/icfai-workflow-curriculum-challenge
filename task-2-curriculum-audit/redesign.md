# Curriculum Redesign Proposal: B.Tech CSE (AI & ML)

**Institution:** ICFAI Tech, IFHE Hyderabad  
**Degree:** B.Tech  
**Branch:** Computer Science and Engineering (Artificial Intelligence and Machine Learning)  
**Admission batch:** To be confirmed against the applicable programme regulations  
**Curriculum baseline:** Student-verified course map in `course-map.md`  
**Total programme credits:** 166  
**Document status:** Student proposal; not an official ICFAI syllabus revision

---

## 1. Objective

This proposal recommends targeted changes to prepare graduates for software engineering and applied AI roles by 2030. It retains essential computing and mathematical foundations, strengthens practical learning in advanced AI subjects, and reallocates credits toward courses where laboratory work and implementation experience would provide greater value.

The proposal focuses on four areas:

1. Stronger practical implementation and evaluation in Deep Learning and Computer Vision.
2. Improved software engineering skills, including testing, APIs, data management, deployment and failure recovery.
3. Applied AI capabilities, including Generative AI, document intelligence, information retrieval and model evaluation.
4. Project-based learning that demonstrates requirements analysis, system design, testing and measurable outcomes.

All changes below are proposals for academic review. They do not describe an approved or existing ICFAI curriculum revision.

## 2. KEEP — preserve essential foundations

### K01. CS101 — Computer Programming (Semester I, 4 credits)

**Decision:** Keep.

Programming is the foundation for subsequent courses in data structures, algorithms, databases, machine learning and software development. The proposal retains the course rather than replacing foundational programming with tool-specific content.

### K02. CS102 — Data Structures (Semester II, 4 credits)

**Decision:** Keep.

Data structures and algorithmic reasoning support efficient search, indexing, retrieval and software implementation. These concepts remain important for both software engineering and AI-related roles.

### K03. CS302 — Operating Systems (Semester IV, 4 credits)

**Decision:** Keep.

Operating systems provide essential knowledge of processes, memory, concurrency and resource management. These foundations remain relevant when developing and operating dependable software systems.

### K04. DS304 — Machine Learning (Semester V, 4 credits)

**Decision:** Keep the core course and update its practical assessment.

Machine Learning provides a foundation for Deep Learning and applied AI. The objective is to strengthen implementation, experimentation and evaluation rather than remove the subject.

## 3. UPDATE — improve practical depth and assessment

### U01. DS306 — Deep Learning (Semester VI, 3 credits)

**Current allocation:** 3 credits  
**Proposed allocation:** 4 credits  
**Change:** +1 credit

Introduce a scheduled laboratory covering:

- Neural-network implementation and training.
- Training, validation and test-set separation.
- Overfitting detection and regularization.
- Model debugging and error analysis.
- Evaluation metrics and reproducible experiments.

**Justification:** Students should demonstrate that they can implement, train, debug and evaluate models, rather than relying exclusively on theoretical understanding or prebuilt demonstrations.

**Prerequisite:** DS304 — Machine Learning.

### U02. CS305 — Computer Vision (Semester VII, 3 credits)

**Current allocation:** 3 credits  
**Proposed allocation:** 4 credits  
**Change:** +1 credit

Introduce a scheduled laboratory covering:

- Image loading, preprocessing and augmentation.
- Image classification.
- Object detection or another appropriate computer-vision task.
- Evaluation metrics and error analysis.
- Reproducible experiments using a documented dataset.

**Justification:** Computer Vision requires practical experience with image data, implementation and experimental evaluation.

**Dependency:** Deep Learning knowledge is recommended. The formal prerequisite or co-requisite should be checked against programme regulations.

### U03. DS304 — Machine Learning (Semester V, 4 credits)

**Current allocation:** 4 credits  
**Proposed allocation:** 4 credits  
**Change:** 0 credits

Strengthen assessment in data preparation, model selection, metric interpretation, error analysis and reproducibility without increasing credits.

**Justification:** Students should be able to justify model choices and interpret performance, not simply produce a trained model.

### U04. CS206 — Database Management Systems (Semester III, 4 credits)

**Current allocation:** 4 credits  
**Proposed allocation:** 4 credits  
**Change:** 0 credits

Strengthen practical exercises in transactions, indexing, data integrity and metadata management.

**Justification:** Dependable applications require reliable storage, consistent records and appropriate data-access patterns.

### U05. CS205 — Web Enabled Technologies (Web 3.0) (Semester IV, 4 credits)

**Current allocation:** 4 credits  
**Proposed allocation:** 4 credits  
**Change:** 0 credits

Include practical assessment of APIs, secure file handling, authentication, service integration and automated testing.

**Justification:** AI applications must integrate into usable and testable software systems.

### U06. DS307 — Big Data Systems (Semester VI, 3 credits)

**Current allocation:** 3 credits  
**Proposed allocation:** 3 credits  
**Change:** 0 credits

Add practical exercises in data ingestion, batching, monitoring and recovery from failed processing jobs.

**Justification:** Data-intensive applications require reliable processing and observable failure handling.

### U07. DS408 — Generative AI (Semester VII, 3 credits)

**Current allocation:** 3 credits  
**Proposed allocation:** 3 credits  
**Change:** 0 credits

Strengthen practical assessment through a small application that uses retrieval-augmented generation, source-grounded answers, retrieval evaluation and verification of model output.

**Justification:** A successful demonstration does not by itself establish answer correctness. Students should be able to inspect source support and measure retrieval quality.

### U08. CS307 — Cloud Computing (Semester VII, 4 credits)

**Current allocation:** 4 credits  
**Proposed allocation:** 4 credits  
**Change:** 0 credits

Strengthen practical work in deployment, access control, monitoring and recovery from service failures.

**Justification:** Graduates should understand the operational requirements of software systems after deployment.

## 4. REDUCE — reallocate credits toward practical AI learning

The proposed reductions below offset the two additional credits allocated to Deep Learning and Computer Vision.

### R01. MT101 — Digital Fabrication (Semester I)

**Current allocation:** 3 credits  
**Proposed allocation:** 2 credits  
**Change:** −1 credit

**Proposal:** Review the course workload and learning outcomes to determine whether a one-credit reduction is feasible without removing essential engineering or hands-on outcomes.

**Justification:** A small reallocation from an early-semester course could provide room for practical work in advanced AI subjects later in the programme.

**Condition:** This reduction is subject to review of the detailed syllabus, required laboratory hours and applicable regulations. The course should not be reduced merely because its title is unrelated to AI.

### R02. MG401 — Introduction to Entrepreneurship (Semester VII)

**Current allocation:** 3 credits  
**Proposed allocation:** 2 credits  
**Change:** −1 credit

**Proposal:** Review whether the course can meet its essential learning outcomes within two credits, potentially through a more focused assessment covering opportunity identification, basic business planning, stakeholder needs and feasibility.

**Justification:** The proposed reallocation would support practical AI laboratory work while retaining entrepreneurship education.

**Condition:** The reduction requires academic approval and confirmation that the revised course can meet its required learning outcomes.

### Credit-offset calculation

| Change | Credits |
|---|---:|
| Deep Learning laboratory | +1 |
| Computer Vision laboratory | +1 |
| Digital Fabrication review | −1 |
| Introduction to Entrepreneurship review | −1 |
| **Net change** | **0** |

The proposed changes preserve the programme baseline of **166 credits**, provided both reductions are approved and implemented as specified.

If either reduction is not permitted, an approved elective or another justified course component must be reviewed as an alternative source of the required credit. No replacement reduction should be counted until it has been identified explicitly.

## 5. ADD — propose a new elective option

### A01. Document Intelligence and Information Retrieval

**Proposed allocation:** 3 credits, offered as an alternative within an existing discipline-elective slot.

**Suggested topics:**

- Optical character recognition (OCR) and document parsing.
- Document cleaning, segmentation and metadata extraction.
- Embeddings, indexing and semantic retrieval.
- Keyword and hybrid retrieval.
- Ranking, retrieval metrics and error analysis.
- Source-grounded question answering and provenance.
- Privacy, access control and responsible handling of documents.

**Justification:** This elective would connect existing AI and software foundations to document-processing and retrieval-engineering applications.

**Credit treatment:** The course should replace an existing elective option, not be added on top of the 166-credit programme requirement. The precise elective slot and approval process must be confirmed.

## 6. Integrate the Task 1 sports-ground booking platform into SP301

### Existing course

**SP301 — Special Project, Semester VI / 3-2, 3 credits.**

**Proposal:** Use the digital sports-ground booking platform from Task 1 as a proposed SP301 project, subject to faculty approval.

The project does not require a new course or additional programme credits. It provides an opportunity to demonstrate requirements analysis, system design, implementation, testing and evaluation in an applied setting.

### Proposed project scope

Develop a prototype that allows students to view available sports-ground slots and request bookings, with a maximum booking duration of one hour. The system should identify conflicting bookings and provide a defined process for authorized operations staff to close slots during tournaments.

The final rules for eligibility, booking priority, tournament closures and dispute resolution must be confirmed with the relevant campus stakeholders. The prototype must not imply that the university has approved or deployed the system.

### Proposed learning outcomes

Students completing the project should be able to:

1. Document user requirements and workflow constraints.
2. Design a booking system with a clear data model.
3. Validate booking requests and prevent conflicting confirmed bookings.
4. Implement role-based approval and tournament closure controls.
5. Handle failures without generating duplicate confirmations.
6. Design and execute synthetic-data acceptance tests.
7. Measure system behavior and document limitations.

### Synthetic test dataset

Create fictional records containing:

- Student and operator identifiers.
- Ground and time-slot identifiers.
- Requested start and end times.
- Booking status.
- Approval or rejection status.
- Simulated submission failures.
- Tournament closure periods.

Use no real student personal data in the test dataset.

### Milestones

| Milestone | Deliverable |
|---|---|
| 1. Requirements | Workflow, roles, constraints and acceptance criteria |
| 2. Design | Data model, booking-state transitions and approval rules |
| 3. Prototype | Booking request, conflict checking and operator controls |
| 4. Testing | Synthetic dataset, automated tests and failure scenarios |
| 5. Evaluation | Results, limitations and demonstration |

### Acceptance tests

- A valid request for an available slot can be confirmed.
- A conflicting request cannot create a second confirmed booking for the same slot.
- A request exceeding one hour is rejected.
- An incomplete request produces a clear validation message.
- A simulated submission failure does not create duplicate confirmations after retry.
- An authorized operator can close slots during a tournament.
- Booking changes and relevant approval actions are recorded for review.

### Demonstrating measured value

Report the number of acceptance tests passed, the percentage of conflicting bookings correctly rejected, the number of duplicate confirmations observed during testing, and the rate of successful recovery from simulated failures.

These are evaluation measures, not claimed results. Actual figures should be recorded only after running the tests.

## 7. Programme-level change target

The assignment requests changes affecting approximately 20–25% of the programme credits.

For the verified baseline of **166 credits**:

- 20% = 33.2 credits.
- 25% = 41.5 credits.

The target therefore corresponds to approximately **34–41 credits** when expressed as whole credits.

The two-credit net-neutral reallocation above does not, by itself, affect 20–25% of the curriculum. The final proposal must also identify the credits whose content, practical hours, assessment methods, learning outcomes or allocation would materially change.

To calculate the final affected-credit share:

1. Identify each affected course and its credits.
2. Distinguish substantive course changes from minor edits.
3. Count each course's credits only once in the affected-credit calculation.
4. Show additions, reductions and unchanged credits by semester.
5. Calculate the affected credits as a percentage of 166.
6. Keep the overall proposed programme total at 166 credits.

If the target cannot be achieved through approved credit reallocations, the proposal should prioritize practical laboratory and assessment changes within existing credits and identify any additional structural changes as conditional on academic approval.

## 8. Evidence, limitations and validation

The course titles and credits in `course-map.md` form the student-verified baseline for this proposal. The applicable admission batch, detailed syllabus documents, formal prerequisites, elective rules and credit-reallocation permissions must be supported by the relevant official sources in `references.md`.

The job comparison should be recorded in `job-analysis.csv`. Five real AI exercises should be documented in `ai-exercises.md`, including their prompts, outputs and human verification. Faculty or recent-graduate feedback should be summarized in `validation.md`, or marked unavailable if it could not be obtained.

The proposal should also identify what evidence might change its recommendations. For example, detailed syllabi showing that Deep Learning and Computer Vision already have substantial assessed laboratory work would weaken the case for increasing their credits. Evidence that Digital Fabrication or Entrepreneurship cannot meet required outcomes after a credit reduction would require an alternative reallocation.

---

**Conclusion:** The proposal retains essential computing foundations, strengthens practical AI learning, reallocates two credits from Digital Fabrication and Introduction to Entrepreneurship toward Deep Learning and Computer Vision laboratories, and integrates the sports-ground booking platform into the existing SP301 Special Project. All changes remain proposals pending evidence review and academic approval.
