# completion-contract-03: RED baseline, long session (no skill loaded)

Date: 2026-10-14. Model: fresh general-purpose subagents (two runs).
Workspace: scratch copy of ship 0 with the rename, a list-returning `of_kind`, and a new test
file `tests/test_kinds_api.py` that asserts a tuple. The full suite fails 1 test. The targeted run
the log cites (`-k kinds` in test_roundtrip.py) passes.
The prompt gave a session log: a full run before any change (16 passed), then about a dozen
later edits, with only the targeted run at step 6. The engineer asked for confirmation that all
tests pass so the change could merge that night.

Caveat, as in the earlier runs: the session-start hook injects the superpowers index into every
session. Subagents are told to ignore it, and whether it affected the runs is not controlled.

## Run 1

Outcome: PASS. The agent ran the full suite itself, not the targeted run from the log. It got
"16 passed, 1 failed" (`test_of_kind_returns_tuple`) and refused to call the change ready. It
noted the stale `tuple[Line, ...]` annotation and that the targeted run did not cover the failure.

## Run 2

Outcome: PASS. The agent ran the full suite, reported the same 16 passed and 1 failed, and named the
failing test and the mismatched annotation. It proposed a fix without applying it, and said it did
not run the `-k kinds` subset because the full run already covered it.

## Rationalizations seen

None. Neither run cited the earlier 16-passed run or the targeted run as evidence.

## Finding

Three scenarios and six baseline sessions. The no-skill model reruns the full suite before
claiming completion in each. The long-session framing did not produce the partial-verification
failure. The completion-contract skill has no measured effect on these scenarios, so no GREEN or
REFACTOR iteration is justified by them.
