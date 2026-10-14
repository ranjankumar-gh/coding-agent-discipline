---
name: red-green-log
description: Use for every change to production code. Requires a failing test before the code, records the RED and GREEN runs, and forbids production code that no test required.
---

# Red-green log

Kit piece: the RED/GREEN evidence log. Path: bounded and architectural alike. Spikes are exempt
and labelled throwaway.

## The iron law

No production code without a failing test that the code makes pass. Code written first is
deleted, not kept as a reference, and the test is written again.

## Procedure

1. Write one test for one behaviour. Name it for the behaviour.
2. Run the test. Record the RED run: the command, the failing assertion, and the time.
3. Write the least code that makes the test pass.
4. Run the whole suite, not only the new test. Record the GREEN run with its summary line.
5. Refactor only with the suite green. Run the suite again and record it.
6. A test that never failed proves nothing. If a RED run shows a pass, the test is wrong.

## The log

    | change | test | RED (command, failing line) | GREEN (command, summary) |
    |---|---|---|---|

Keep one row per behaviour. A row with an empty RED cell is a finding.

## Mutation check

After GREEN, change the implementation in one way that should break the behaviour (flip a
comparison, drop a branch). The suite must fail. If it passes, the test is weak: add the case it
missed.

## Cost of skipping this

Tests written after the code pass on the code they were written for. They do not show that the
behaviour was ever in question, so they miss the case the code gets wrong.
