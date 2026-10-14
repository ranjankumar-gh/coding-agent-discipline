---
name: task-brief
description: Use when handing one task of an approved plan to a fresh subagent. Writes the task as a file the subagent reads, never pasted history, and defines the implementer's status vocabulary.
---

# Task brief

Kit piece: the task-brief and implementer templates. Path: architectural (a plan with independent
tasks). Bounded changes do not need dispatch.

## Rules

- Write the brief to a file. The subagent reads the file. Do not paste conversation history into
  the prompt.
- The brief contains: the task's text from the plan, the Global Constraints copied from the spec,
  the Consumes and Produces interfaces, the files it may touch, the verify command, and the
  statuses below.
- The controller does not fix code. If the implementer's output is wrong, a new brief is written
  and a new implementer is dispatched.
- Name the model. The least capable model that is adequate for the task is named in the brief.

## Implementer statuses

The implementer ends its report with exactly one of:

- `DONE`: the task's verify command ran and passed, and the output is included.
- `DONE_WITH_CONCERNS`: done, with a concern the controller must read before the next task.
- `BLOCKED`: the task cannot be finished. The report names the missing input.
- `NEEDS_CONTEXT`: the brief does not say enough. The report names the question.

## Implementer template

    Task: <name>
    Read: <brief path>
    Touch only: <files>
    Done when: <verify command> passes, and you have pasted its output.
    Report: one of DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT, then the evidence.

## Cost of skipping this

A pasted history grows with every task, and the implementer spends its context on what was
already decided. A file brief is read once, and its size is the task's size.
