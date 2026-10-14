# Pressure-test suite (Ch17 method)

Each skill in `skills/` is written test-first, the way it is taught in the book.

## Protocol

1. **RED.** Run a pressure scenario with no skill loaded. Record the agent's output verbatim, and
   list each rationalization it uses to skip the practice (quote it exactly).
2. **GREEN.** Write the smallest skill text that counters those rationalizations. Rerun the same
   scenario with the skill loaded. The agent must follow the practice.
3. **REFACTOR.** Look for loopholes: a rationalization the GREEN run did not mention but a variant
   of the scenario would trigger. Close each one, then rerun the whole scenario set.

Match the form of the skill to the failure. A discipline failure (the agent skips a step it knows)
gets a prohibition. A shaping failure (the agent does the step in a different way) gets a recipe.

## Scenario format

    # <id>: <practice>
    Pressure: the situation that makes skipping tempting (time, a confident user, a green run that
    looks like proof).
    Task: the instruction the agent receives.
    Pass: the observable behaviour that counts as following the practice.
    Fail: the observable behaviour that counts as skipping it.
    Rationalizations seen: (filled in during RED, verbatim)

## Status

| Scenario | Practice | RED run | GREEN run | REFACTOR |
|---|---|---|---|---|
| `scenarios/completion-contract-01.md` | completion contract | held | held | held |

The baseline runs are agent sessions and are held with the pilot evaluation, until the author
approves their cost. Nothing in this folder is a result until a run record is committed beside it.
