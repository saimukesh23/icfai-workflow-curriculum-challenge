# AI-Assisted Learning Exercises: Five Curriculum Subjects

**Programme:** B.Tech CSE (AI & ML)  
**Institution:** ICFAI Tech, IFHE Hyderabad  
**Curriculum reference:** `course-map.md`  
**Exercise record date:** 24 October 2026  
**AI model:** ChatGPT —GPT-6  
**Purpose:** Examine how AI can support learning in five subjects and document how its answers can be independently checked.

> **Record note:** The prompts and outputs below were prepared and checked as part of this exercise record. The verification describes the checks performed on the examples; it does not imply that external applications, university systems or model-training experiments were run.

---

## Exercise 1 — Data Structures (CS102, Semester II)

### Task

Use AI to explain and check a Java stack implementation for balanced parentheses.

### Prompt used

> Explain how to check whether parentheses in a string are balanced using a stack in Java. Provide a short method that handles `()`, `{}` and `[]`. Test it on `"{[()]}"`, `"([)]"` and `"((("`. Explain the time complexity and why a stack is appropriate.

### AI output

A stack follows the Last In, First Out (LIFO) principle. When an opening bracket appears, push it onto the stack. When a closing bracket appears, check whether the stack's top contains the corresponding opening bracket. If not, the expression is invalid. At the end, the stack must be empty.

```java
import java.util.*;

public class Main {
    static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (stack.isEmpty()) return false;

                char top = stack.pop();

                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
```

Expected results:

| Input | Output |
|---|---|
| `{[()]}` | `true` |
| `([)]` | `false` |
| `(((` | `false` |

**Complexity:** \(O(n)\) time, because each character is processed at most once; \(O(n)\) auxiliary space in the worst case for the stack.

### Verification

- Traced the stack operations for `{[()]}`: every closing bracket matches the most recent opening bracket, leaving an empty stack.
- Traced `([)]`: `)` encounters `[` at the top, so the expression is rejected.
- Traced `(((`: the stack remains nonempty after processing all characters, so the expression is rejected.
- Checked the complexity against the single-pass algorithm and its maximum stack size.

**Verification result:** The stated outputs and complexity are consistent with the algorithm for these test cases.

**What I learned:** A stack is appropriate when the most recently opened structure must be closed first. The trace also shows why simply counting opening and closing brackets is insufficient.

---

## Exercise 2 — Database Management Systems (CS206, Semester III)

### Task

Use AI to write and validate a SQL query that finds students with more than one booking.

### Prompt used

> Given a table `Bookings(booking_id, student_id, ground_id, status)`, write a SQL query to find students with more than one confirmed booking. Explain the role of `WHERE`, `GROUP BY` and `HAVING`. Use a small example to check the result.

### AI output

```sql
SELECT student_id, COUNT(*) AS confirmed_bookings
FROM Bookings
WHERE status = 'CONFIRMED'
GROUP BY student_id
HAVING COUNT(*) > 1;
```

Example data:

| booking_id | student_id | ground_id | status |
|---|---|---|---|
| 101 | S01 | G1 | CONFIRMED |
| 102 | S01 | G2 | CONFIRMED |
| 103 | S02 | G1 | CONFIRMED |
| 104 | S01 | G1 | CANCELLED |
| 105 | S03 | G2 | CONFIRMED |
| 106 | S03 | G2 | CONFIRMED |

Expected output:

| student_id | confirmed_bookings |
|---|---:|
| S01 | 2 |
| S03 | 2 |

`WHERE` filters individual rows before grouping. `GROUP BY` forms groups by student. `HAVING` filters those groups after aggregation, retaining only students whose confirmed-booking count exceeds one.

### Verification

- Counted only rows with `status = 'CONFIRMED'`.
- S01 has two confirmed bookings; its cancelled booking is excluded.
- S02 has one confirmed booking and is excluded.
- S03 has two confirmed bookings and is included.
- Checked that `HAVING COUNT(*) > 1` is applied after grouping.

**Verification result:** The query and expected output are consistent with the example data.

**Limitation:** This query identifies students with multiple confirmed bookings, not necessarily conflicting bookings. Detecting time conflicts would require booking start and end times.

**What I learned:** Aggregation and row filtering serve different purposes. I also learned that a query's output must be interpreted according to the fields actually available in the database.

---

## Exercise 3 — Machine Learning (DS304, Semester V)

### Task

Use AI to calculate classification metrics from a confusion matrix and interpret the results.

### Prompt used

> A binary classifier produces TP = 40, FP = 10, FN = 5 and TN = 45. Calculate accuracy, precision, recall and F1-score. Show the formulas, intermediate calculations and final percentages. Explain what the metrics mean.

### AI output

The total number of predictions is:

\[
N = TP + FP + FN + TN = 40+10+5+45=100
\]

**Accuracy**

\[
\frac{TP+TN}{N}=\frac{40+45}{100}=0.85
\]

Accuracy = **85%**

**Precision**

\[
\frac{TP}{TP+FP}=\frac{40}{40+10}=0.80
\]

Precision = **80%**

**Recall**

\[
\frac{TP}{TP+FN}=\frac{40}{40+5}
\approx 0.8889
\]

Recall = **88.89%**

**F1-score**

\[
F1=2\frac{Precision \times Recall}{Precision+Recall}
\]

\[
F1=2\frac{0.80 \times 0.8889}{0.80+0.8889}
\approx 0.8421
\]

F1-score = **84.21%**

### Verification

- Recomputed the total from the four confusion-matrix cells; it equals 100.
- Checked accuracy using the 40 true positives and 45 true negatives.
- Checked precision using the 10 false positives.
- Checked recall using the 5 false negatives.
- Substituted the unrounded precision and recall into the F1 formula before rounding.

**Verification result:** All four metric values are arithmetically consistent with the given confusion matrix.

**What I learned:** Precision measures how many predicted positives are correct, while recall measures how many actual positives are found. The appropriate metric depends on the consequences of false positives and false negatives.

---

## Exercise 4 — Deep Learning (DS306, Semester VI)

### Task

Use AI to identify data leakage in a proposed model-training workflow.

### Prompt used

> I am building a deep-learning classifier. I split my dataset into training and test sets, normalize the entire dataset before splitting, and use test-set performance repeatedly to choose model architecture and hyperparameters. Identify possible data leakage, explain why it matters, and propose a corrected workflow.

### AI output

Two risks are present:

1. **Preprocessing leakage:** Fitting a normalization transformation using the entire dataset allows information from the test set to influence preprocessing. For example, the overall mean and standard deviation may incorporate test examples.
2. **Test-set overuse:** Repeatedly selecting architectures and hyperparameters based on test performance indirectly uses the test set for model selection. The final test score may no longer provide an unbiased estimate of performance on unseen data.

A safer workflow is:

1. Split the data into training, validation and test sets.
2. Fit preprocessing transformations on the training set only.
3. Apply the fitted transformations to validation and test data without refitting on them.
4. Use the validation set for model selection and hyperparameter tuning.
5. Evaluate the final selected model on the test set once the development decisions are complete.

For datasets containing multiple samples from the same person, device or source, use a group-aware split where appropriate to reduce leakage between related examples.

### Verification

- Checked the definition of data leakage: information unavailable at the intended prediction time must not influence model fitting or selection.
- Confirmed that fitting preprocessing on training data only prevents test-set statistics from entering that transformation.
- Confirmed that a validation set is the appropriate resource for iterative model selection.
- Checked the additional caveat that random splitting may still leak information when samples are correlated or duplicated.

**Verification result:** The identified risks and proposed workflow are consistent with standard machine-learning evaluation practice.

**Limitation:** No neural network was trained and no dataset was evaluated in this exercise. It is a conceptual workflow audit, not an experimental performance result.

**What I learned:** A model can achieve a strong test score without providing a reliable estimate of generalization if information from the test set influences preprocessing or development decisions.

---

## Exercise 5 — Generative AI (DS408, Semester VII)

### Task

Use AI to answer a question from a small supplied source and check whether the answer is grounded in that source.

### Prompt used

> Use only this source: “The campus sports ground can be booked for a maximum of 60 minutes per reservation. During approved tournaments, the sports-club operations team may close booking slots. The source does not specify booking priority or the procedure for resolving disputes.”  
>
> Question: What is the maximum booking duration, who can close slots during approved tournaments, and what is the dispute-resolution procedure? Do not invent missing information. Clearly state which details are not provided.

### AI output

- **Maximum booking duration:** 60 minutes per reservation.
- **Who may close booking slots during approved tournaments:** The sports-club operations team.
- **Dispute-resolution procedure:** The supplied source does not specify one, so the procedure cannot be established from this information.

### Verification

| Claim | Source evidence | Result |
|---|---|---|
| Maximum booking duration is 60 minutes | Explicitly stated in the source | Supported |
| Sports-club operations team may close slots during approved tournaments | Explicitly stated in the source | Supported |
| Dispute-resolution procedure is unspecified | Source explicitly says it is not specified | Supported |

**Verification result:** All three statements are grounded in the supplied source. The answer does not invent a dispute-resolution policy.

**Limitation:** This checks one response against a short, user-provided passage. It does not establish the reliability of a complete RAG system or prove that the proposed campus booking rules have been approved.

**What I learned:** Generative AI should distinguish source-supported facts from missing information. In a retrieval-based system, citations and source checks help identify unsupported claims.

---

## Overall reflection

These five exercises demonstrate different ways AI can support learning:

- **Data Structures:** explain algorithms and produce testable examples.
- **Database Management Systems:** draft queries and validate aggregation logic.
- **Machine Learning:** calculate and interpret evaluation metrics.
- **Deep Learning:** review training workflows for leakage and evaluation risks.
- **Generative AI:** produce source-grounded answers while identifying missing information.

The main lesson is that an AI-generated answer is a starting point, not proof of correctness. Verification should be specific to the subject: dry-running code, checking SQL results against sample records, recalculating formulas, reviewing model-evaluation methodology and tracing generated claims back to their source.

These exercises support the curriculum proposal by illustrating how assessment can require both AI-assisted work and independent verification. They do not establish that the current courses lack these activities; that conclusion would require reviewing the detailed course syllabi and assessments.

## Reproducibility record

| Field | Record |
|---|---|
| Model | ChatGPT — GPT-6 |
| Preparation date | 24 October 2026 |
| Subjects covered | Data Structures, DBMS, Machine Learning, Deep Learning, Generative AI |
| Exercise type | Code reasoning, SQL validation, metric calculation, workflow audit, source-grounded generation |
| External datasets used | None |
| Model training performed | No |
| Application deployment performed | No |
| Verification | Manual reasoning and consistency checks documented per exercise |

