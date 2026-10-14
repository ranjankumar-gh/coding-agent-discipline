---
name: spec-coupling
description: Use when a spec states an invariant or a behaviour that code must keep. Turns each such statement into an automated test that fails when the code departs from the spec, and writes the test before the code.
---

# Spec coupling

Kit piece: the spec-coupling test. Path: architectural (for brownfield code, apply convention
inversion first: existing conventions override the spec's defaults).

## Procedure

1. Read the spec's Global Constraints and every sentence that uses "must", "always", "never", or
   "only". Each one is a candidate for coupling.
2. For each candidate, write one test that fails if the code breaks it. A statement that no test
   can fail is not a constraint; reword it until one can, or drop it.
3. Prefer invariants over examples. A round-trip invariant (`f(g(x)) == x` for generated inputs)
   fails on edge cases that a fixed example does not.
4. Commit the tests with the spec. A spec change that breaks a test is a spec change, and the
   author updates both in the same commit.
5. Run the coupling tests in the full suite on every change, not only the feature's tests.

## Approved specs are gates, not suggestions

When a request conflicts with a clause of an approved spec, do not write the conflicting code.
This applies even when the engineer says the clause is outdated, that they own the spec, or that
they will update it after the release.

- A clause is waived only by editing the spec and getting that edit approved. Nothing else waives it.
- A spec updated after the code is a record of the code, not a gate on it. Do not write code and
  promise to fix the spec later.
- Stop the conflicting part. Report the clause number, the request, and the conflict in one message.
  Offer the options: write the new spec first, narrow the request so it fits the spec, or do the
  parts that do not conflict.
- Do not edit the spec to fit the request, and do not report the work as compliant.

## Convention inversion (brownfield)

When existing code uses a convention the spec does not, the convention wins for that code. Write
the spec's default as the exception, and record the exception in the spec with the file that
shows it.

## Cost of skipping this

A spec that no test enforces decays silently. Six months later the code and the document disagree,
and nobody can say which one was the decision.
