---
name: run-state
description: Use for any long-running or looping agent run. Keeps progress in a state file outside the context window, trusts git over recollection, and uses a completion judge that is not the working model.
---

# Run state

Kit piece: the run-state schema. Path: architectural (long runs) and bounded (any fix loop with a
retry cap).

## Three ingredients

1. **Externalized state.** Progress lives in a file, not in the conversation. A new context reads
   the file and continues.
2. **Disposable context.** Each iteration starts from the state file and the repository. Nothing is
   carried over from the previous iteration except what the file records.
3. **A completion judge that is not the working model.** Completion is decided by a command (the
   suite, the check), and by a fresh reader for anything a command cannot decide.

## The state file

    {
      "run_id": "...",
      "goal": "<one sentence, from the spec>",
      "iteration": 0,
      "budget": {"max_iterations": 0, "max_spend_usd": 0},
      "last_commit": "<sha>",
      "done": [{"task": "...", "evidence": "<command and summary>"}],
      "open": [{"task": "...", "blocked_by": "..."}],
      "rulings": "<path to ruling ledger>"
    }

## Rules

- Trust git over recollection. If the state file and `git log` disagree, the log wins and the file
  is corrected.
- A fix loop has a cap. At the cap it stops and writes the state file. A circuit breaker bounds
  spend and retries. It is not a security control.
- Escalate the model only after a failed attempt, never before.
- The judge reads the state file and the repository. It does not read the working model's summary.

## Cost of skipping this

A loop whose state lives in its context stops working at the first compaction, and restarts from
its own summary. The summary is the thing being checked.
