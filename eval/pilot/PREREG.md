# Pilot evaluation: pre-registration

Registered 2026-10-14, before any session runs. Changes after this date are recorded as deviations
in `RESULTS.md`, not made silently.

## Question

Does the skill pack (`skills/`, pilot pack v0, tree hash recorded in `RESULTS.md`) raise the rate at
which a coding agent completes a flowround edit task correctly, compared with the same agent and
brief without the pack?

## Design

- Five held-out tasks, T1 to T5 (rename a node, add an edge, relabel an edge, remove a node,
  normalize line endings). Hidden tests and briefs are in a private repository and are never
  published here. The task descriptions are not reproduced in this repository.
- Two arms: **with** (the workspace contains `skills/`, and the brief says the pack is available)
  and **without** (the workspace has no `skills/` and no `eval/`).
- Five repetitions per task per arm: 5 × 5 × 2 = **50 sessions**.
- Runs are interleaved across arms and tasks, so no arm runs as a block.
- Each session gets a fresh workspace: a clean `git archive` of this repository's HEAD at the time
  of the run. Both arms have `eval/` removed. The without arm also has `skills/` removed, so the
  with arm differs only by the pack. Workspaces are not reused across sessions.
- Each session is a fresh general-purpose subagent with the same default model. The brief is
  pasted into the prompt. The prompt does not mention the arm.

## Grading

- Task success is decided only by the hidden tests, run by `grader/run_task.py` from the private
  repository against the candidate's `src/flowround/edit.py`. A model does not grade.
- A session that fails to produce `edit.py` counts as a failure.
- Infrastructure failures (a session that never starts or returns no report) are recorded and
  re-run once. A second infrastructure failure is recorded as missing, not as a failure.

## Metrics

- **Primary:** task success, pass or fail per session.
- **Cost proxy:** subagent tokens and tool uses per session. Billed cost is not reported by the
  subagent tool, so the book cannot claim billed cost from this pilot. This is a stated limit.
- **Turns:** tool uses per session, reported alongside tokens.

## Analysis

- Success rate per arm with a 95% Wilson interval, and per task.
- Difference between arms with an interval. Paired by task, since each task has a fixed brief.
- Tokens and tool uses per arm, median and range.
- Reported as a pilot. The claim is limited to what the intervals support.

## Stop rules

- No expansion beyond 50 sessions in this pilot, and no re-runs of failed sessions for a better
  result. A larger study is a separate pre-registration.

## Known limits

- A subagent could read files outside its workspace, including the private repository, if it looks.
  The prompt says to work only in the workspace. Any observed reference to paths outside the
  workspace is recorded in `RESULTS.md`.
- The briefs are pasted into the prompt, so the with arm reads the skill pack from disk, and the
  without arm does not have it. The two arms therefore differ in more than the pack's text.
- Five tasks is a small set. The result cannot generalize past these tasks or this model.
