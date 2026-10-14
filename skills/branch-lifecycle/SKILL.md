---
name: branch-lifecycle
description: Use before running agents in parallel and when finishing a branch. Isolates each independent problem in its own worktree, runs a baseline test pass first, and finishes with a defined set of options.
---

# Branch lifecycle

Kit piece: the branch lifecycle checklist. Path: architectural (parallel work) and bounded
(finishing any branch).

## Before parallel work

1. Create one git worktree per independent problem domain. Two tasks that touch the same file are
   not independent.
2. Run the full test suite in each new worktree, on the base commit, before any change. Record the
   baseline. Failures in the baseline are pre-existing, and are recorded as such.
3. Give each worktree one agent. An agent does not switch worktrees.

## Limits of isolation

A worktree isolates files and branches. It does not isolate environment variables, credentials, the
network, or the home directory. Security limits are a different control (see the dispatch-safety
skill).

## Finishing a branch

Offer the options the pinned version of the skill defines, and state which one you took. Do not
discard a branch without a typed confirmation that names the branch.

## Stacked and shared checkouts

Stacked branches fail silently when a base changes after the stack is built. Rebase the stack and
rerun the suite on each layer. Two agents never share one checkout.

## Cost of skipping this

Two agents in one checkout overwrite each other's edits with no error. The suite runs green on
whichever edit landed last.
