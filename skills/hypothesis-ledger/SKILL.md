---
name: hypothesis-ledger
description: Use when a test fails or behaviour is unexpected, before proposing any fix. Requires root cause investigation, one hypothesis at a time, and a stop rule after three failed fixes.
---

# Hypothesis ledger

Kit piece: the hypothesis ledger. Path: bounded (a one-file fix) and architectural (a failure
that crosses components).

## Phases

1. **Investigate.** Reproduce the failure on a clean tree. Read the full error. Record the exact
   command and output. Do not call a failure "pre-existing" until it reproduces on a clean checkout
   of the base commit.
2. **Compare patterns.** Find a working case that is close to the failing one. List every
   difference between them.
3. **One hypothesis at a time.** State one cause that would explain the difference. Test it with
   the smallest change that could confirm or refute it. Revert the change before the next
   hypothesis.
4. **Fix test-first.** Write the failing test for the root cause, then the fix.

## The ledger

    | # | hypothesis | the test that would refute it | result | fix attempted |
    |---|---|---|---|---|

## The three-fix rule

If three fixes in a row have failed, stop. Three failed fixes means the design is wrong, not
the code. Return to the design spec and say which assumption failed.

## Cost of skipping this

Each unrecorded guess changes the code, and the next failure is then a failure of the code plus
the guess. After five guesses the original cause is unrecoverable.
