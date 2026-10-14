---
name: completion-contract
description: Use before saying any work is done, fixed, passing, or complete. Requires a command run in this session, its output read, and the claim made only from that output.
---

# Completion contract

Kit piece: the completion contract. Path: every path.

## The gate

Before a completion claim, do all of these in order, in the same message:

1. **Identify** the command that proves the claim (the test suite, the build, the check that
   exercises the real effect).
2. **Run** it now, in this session, against the current tree.
3. **Read** the full output, including the exit code and the summary line.
4. **Verify** the output supports the claim. A green status from a different command does not.
5. **Claim** only what the output shows, and grade the evidence:
   - *ran*: the command ran and passed;
   - *checked statically*: a reading or a linter, with no run;
   - *declared unverified*: nothing above was done.

## Check the effect, not the status

A passing suite proves what the suite checks. When the claim is about behaviour (a file is
written, a request is sent, a page renders), run the thing and look at its effect.

## Stopping condition

The loop stops when the gate passes, not when the agent is satisfied. If the gate cannot run,
the claim is "declared unverified" and the reason is written next to it.

## Cost of skipping this

"Tests pass" from a run that was not repeated after the last edit is a claim with no evidence
behind it. It is also the most common way a reviewer finds a regression the author had already
declared fixed.
