---
name: ruling-ledger
description: Use when executing an approved plan inline without check-ins. Records every autonomous decision as a ruling with what was decided, why, and the cost if it is wrong, and stops only for the four listed reasons.
---

# Ruling ledger

Kit piece: the ruling ledger. Path: architectural (plan execution).

## Stop reasons

Stop and ask only for one of these:

1. The spec contradicts itself, and no reading is consistent with the success criteria.
2. The task needs an action that is outward-facing or hard to reverse (publishing, deleting shared
   data, spending beyond the budget).
3. The verify command fails in a way the ledger's fixes have not resolved after three attempts.
4. A required input is missing and cannot be derived from the repository.

Everything else is a ruling.

## Recording a ruling

    | # | question | ruling | why | cost if wrong | reversible? |
    |---|---|---|---|---|---|

- *question*: the decision the plan did not settle.
- *ruling*: the choice made.
- *why*: the line in the spec or the constraint that decided it.
- *cost if wrong*: what breaks, and how many tasks would need redoing.

## Surfacing

Surface every ruling at the end of the plan, in one list, before the final verify. A reviewer reads
the list first.

## Cost of skipping this

An autonomous decision that is not recorded looks, at review, like an error. The reviewer then
reconstructs the reasoning from the diff, and sometimes reverses a sound decision.
