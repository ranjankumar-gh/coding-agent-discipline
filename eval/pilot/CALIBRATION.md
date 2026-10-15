# Calibration: harder held-out tasks T6 to T10 (no skill)

Date: 2026-10-15. One unassisted session per task, default general-purpose subagent, workspace built
from the public repo's HEAD with no `skills/` and no `eval/`. Grading by the hidden tests in the
private repository. Task briefs and tests are private and are not reproduced here.

| task | result |
|---|---|
| T6 split an edge | PASS (9 of 9) |
| T7 rename with collision refusal | PASS (10 of 10) |
| T8 remove edges between two nodes | PASS (8 of 8) |
| T9 add a node declaration | PASS (9 of 9) |
| T10 set a node label | PASS (8 of 8) |

Reading: the tasks I wrote as harder were not harder for this model. All five passed unassisted on
the first attempt. The failures seen in the pilot came from brief-versus-spec wording, not from the
edit logic. A pilot on tasks of this kind will not separate the two arms, so the pre-registered
pilot is not justified by these tasks as they stand.
