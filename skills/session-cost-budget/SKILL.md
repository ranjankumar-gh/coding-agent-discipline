---
name: session-cost-budget
description: Use to set and check the cost of a discipline session. Counts the injected context, the per-subagent preamble, and the review rounds, and prefers the cheapest model that is adequate, judged by turn count rather than token price.
---

# Session cost budget

Kit piece: the session cost budget. Path: every path; the budget scales with the path.

## What to count

- **Injected session context:** the instructions, skills, and files loaded at session start.
- **Per-subagent preamble:** what each dispatched subagent receives before its task.
- **Review rounds:** each full review pass, multiplied by the number of tasks it covers.
- **Turns:** the number of model turns to finish, not only the tokens of each turn.

## Budget

Set the budget before the session, from the path:

| Path | Injected context | Preamble per subagent | Review rounds |
|---|---|---|---|
| spike | minimal | none | none |
| bounded | one skill | none | one |
| architectural | the skills in use | the task brief | one per task |

Record the budget in the run-state file. Stop and report when the spend reaches it.

## Choosing a model

Prefer the least capable model that passes the task's verify command. Compare models by turns to
pass, not by price per token: a cheaper model that takes four turns can cost more than a dearer one
that takes one.

## Batching

Batch same-shape edits into one change. Each separate edit costs a turn.

## When the discipline is not worth it

A change to one line with a passing test and no interface change does not need the full loop.
Record the decision as a ruling.

## Cost of skipping this

Without a budget, the cost of a method is invisible until the invoice arrives, and the method looks
free because nobody measured it.
