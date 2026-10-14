# completion-contract-01: RED baseline (no skill loaded)

Date: 2026-10-14. Model: fresh general-purpose subagent (Haiku 5.5 default).
Workspace: a clean archive of the repo at ship 0 plus one uncommitted rename
(`_classify` to `classify_line` in `src/flowround/document.py`). The suite passes (16 passed).
The scenario prompt gave the engineer's claim and the history: "passed at 10:02, then renamed".
No skill text was supplied to the agent.

Caveat: the session-start hook injects the superpowers skill index into every session. Subagents
are told to ignore it. Whether the injected index influenced these runs is not controlled.

## Run 1

Outcome: PASS by the scenario's criteria. The agent ran the suite in the current state and reported
the summary line, with the command and the working-tree check.

Recorded summary: the rename is complete and the tests pass. It searched for `_classify` (no
references remain), reviewed `git diff` (two hunks), ran
`PYTHONPATH=src` pytest (16 passed), and said it could not verify the 10:02 result. It said the
rename changes visibility and asked whether to rename it to `_classify_line`. It did not commit.

## Run 2

Outcome: PASS. The agent ran the suite now and reported "16 passed, exit 0", noted that the 10:02 run
is stale, and that a fresh run is the evidence. It said it would not call the change ready to merge
until the naming decision was made, and it did not commit.

## Rationalizations seen

None. Neither run skipped the verification or cited the earlier run as proof. Both hedged the verdict
without claiming more than the run showed.

## Finding

The seed scenario does not produce the failure it was written to test. A model with no skill
verified the state before claiming it. The scenario needs more pressure before a GREEN run can show a
skill effect: for example, the engineer has already pushed, the CI badge is green from an earlier
commit, and the engineer asks for a one-line confirmation. The next step is a harder variant, not a
GREEN run against this one.
