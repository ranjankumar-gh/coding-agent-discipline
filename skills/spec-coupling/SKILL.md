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

## Convention inversion (brownfield)

When existing code uses a convention the spec does not, the convention wins for that code. Write
the spec's default as the exception, and record the exception in the spec with the file that
shows it.

## Cost of skipping this

A spec that no test enforces decays silently. Six months later the code and the document disagree,
and nobody can say which one was the decision.
