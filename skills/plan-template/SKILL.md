---
name: plan-template
description: Use after a design spec is approved and before any implementation, to write an implementation plan for an engineer with no context. Each task is two to five minutes, names exact interfaces, and contains no placeholders.
---

# Plan template

Kit piece: the plan template and the placeholder linter. Path: architectural.

## Rules

- Each task takes two to five minutes to carry out and ends with a verifiable result.
- Give every interface the task touches: what it consumes (Consumes) and what it produces (Produces),
  with exact names and types.
- Copy the spec's Global Constraints into the plan verbatim. Do not summarize them.
- Add a Review Focus line to each task: the inputs that no test exercises yet, which the reviewer
  should probe.
- No placeholders. "TBD", "similar to task 3", "add error handling", and "handle edge cases" are
  defects, not steps.

## Template

    # <Topic> plan
    ## Global constraints (copied from the spec)
    ## Task N: <name>
    Consumes: <name: type>, ...
    Produces: <name: type>, ...
    Steps:
      1. <exact action, file, and expected result>
      2. ...
    Verify: <command and expected output>
    Review focus: <inputs no test exercises yet>

## Placeholder linter

Run before handing the plan over. It fails on any of these strings: `TBD`, `TODO`, `similar to`,
`add error handling`, `handle edge cases`, `etc.`, `as appropriate`. It also fails on a task with
no `Verify:` line, and on a task whose `Consumes:` or `Produces:` names something no other task
produces or consumes.

## Cost of skipping this

A plan written for someone who already knows the codebase skips the one step that a fresh
implementer cannot guess. The implementer then invents an interface, and the mismatch surfaces
two tasks later as a failing integration test.
