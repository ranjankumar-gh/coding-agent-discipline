---
name: reviewer-prompts
description: Use to review a completed task or a finished branch. Runs two verdicts in order, spec compliance first and code quality second, with a reviewer who does not trust the author's report and does not see the author's context.
---

# Reviewer prompts

Kit piece: the reviewer prompt pack. Path: architectural (every dispatched task gets review).

## Two verdicts, in order

1. **Spec compliance.** Does the change do what the spec and the task say, and nothing the spec
   does not say? Classify each finding as *missing* (required, absent), *extra* (present, not
   required), or *misunderstood* (present, does a different thing).
2. **Code quality.** Only after verdict one passes. Is the code correct, clear, and tested at its
   boundaries? Findings name the file and line.

## Standing instructions for every reviewer

- Do not trust the implementer's report. Run the verify command yourself and read its output.
- You are not given the author's conversation. Judge the diff, the spec, and the tests.
- Report what you ran, and what you did not run.
- A finding without a file and line, or without a way to reproduce it, is not a finding.

## Reviewer prompt

    You are reviewing task <N> against the spec at <path>. You have the diff and the spec only.
    Verdict 1 (spec): list missing, extra, and misunderstood items, each with evidence.
    Verdict 2 (quality): only if verdict 1 has no missing or misunderstood items. Name file and line.
    Run: <verify command>. Paste the summary line. Do not trust the implementer's claim.

## Receiving a review

Verify each finding before changing code. Push back with evidence when a finding is wrong. Do not
implement a suggestion you have not checked.

## Cost of skipping this

A reviewer who reads the author's report reviews the report. The bugs in the code are then the
ones the author already believed were fixed.
