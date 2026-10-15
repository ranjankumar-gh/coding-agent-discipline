# Pilot evaluation: results

Design, arms, and analysis plan: `PREREG.md` (committed 2026-10-14 before any session ran).
Pack tree hash (skill pack v0, `skills/`): `b01f0b7d9024e31ddf510f5b82687e618e78188d`.
Repository commit the workspaces were built from: `f2f5fa63fd107914e96d1e9ef7b155c4d5f8b7eb`.
Model: default general-purpose subagent for every session (the same model in both arms).
Tasks T1 to T5 and their hidden tests are in a private repository and are not reproduced here.

## Outcome

Hidden-test grading, 50 sessions (5 tasks × 5 repetitions × 2 arms):

| arm | pass | fail | success | Wilson 95% interval |
|---|---|---|---|---|
| with the skill pack | 24 | 1 | 0.96 (24/25) | 0.80 to 0.99 |
| without the skill pack | 25 | 0 | 1.00 (25/25) | 0.87 to 1.00 |

Per session:

| task | with r1 to r5 | without r1 to r5 |
|---|---|---|
| T1 rename node | P P P P P | P P P P P |
| T2 add edge | P P **F** P P | P P P P P |
| T3 relabel edge | P P P P P | P P P P P |
| T4 remove node | P P P P P | P P P P P |
| T5 normalize endings | P P P P P | P P P P P |

## Reading the result

- **The difference is 4 points, and the intervals overlap.** The pilot shows no detectable effect of
  the skill pack on these tasks. The result cannot support a claim that the pack helps, or that it
  hurts.
- **The tasks are at ceiling.** Without the pack, every session passed. A design that cannot show a
  failure without the pack cannot show a benefit from it. The pack was not tested on the failures it
  targets.
- **The one with-arm failure was a spec refusal, not a wrong edit.** In with r3, T2, the session
  refused the rule that puts a new edge after an unterminated final line. It cited
  `docs/flowround-spec.md`, which says edits must leave bytes outside the edited line unchanged. The
  hidden test expects the brief's rule, so the session failed it. The brief and the spec disagree on
  this case. That is a real inconsistency in the project's own documents, and the pilot exposed it.

## Deviations and incidents (recorded, not hidden)

1. **Workspace contents corrected before any run.** The first set of 50 workspaces kept `eval/` in
   the with arm. Before any session ran, I corrected `PREREG.md` so both arms drop `eval/`, and I
   rebuilt the workspaces from that commit. No session ran on the discarded set.
2. **Stray files.** Several sessions reported writes that landed in a different workspace or did not
   land at all. In at least one case a test file was written into an `r1` workspace, and in another
   a file appeared in an `r2` workspace. Graders copy only `src/` from a candidate workspace and run
   the hidden tests, so no stray test file can change a grade. The stray files were not used.
3. **Background searches.** Two sessions left a filesystem-wide `find` running in the background. Both
   are read-only. One was not stopped.
4. **Token and tool-use counts** were reported by the subagent tool for each session but were not
   aggregated into this file. The cost comparison the pre-registration called for is therefore not
   reported, and the book cannot claim a cost result from this pilot.
5. **Prompt disclosure.** The skill pack was made available by a sentence in the with-arm prompt and
   by the files in `skills/`. The arms also differ in the presence of `skills/`, so the pilot tests
   the pack as a whole and not any single practice.

## What this pilot does and does not establish

- It establishes that the five tasks, as written, do not separate the two arms for this model.
- It does not establish that the skill pack works or fails. A replication needs tasks where the
  unassisted model fails at a meaningful rate, which these are not.
- The hidden-test grader and the task briefs are unchanged. The one finding that comes from the
  project's own documents (the brief's rule 3 against the spec's line rule) should be resolved before
  any further pilot, since it can make a correct spec-following session count as a failure.

## Resolution (2026-10-15)

The brief-versus-spec conflict behind with r3 T2 is resolved in `docs/flowround-spec.md`. The
spec's "bytes outside the edited line are unchanged" rule now carries one stated exception: an
append after an unterminated final line gives that line the dominant ending, and `add_edge` is the
only operation this applies to. The brief's rule 3 is the intended behaviour. The recorded failure
above is kept as it happened. The pilot's hidden tests are unchanged, and the pilot is not re-run.
