---
name: design-spec
description: Use before writing any code for a new feature, subsystem, or change to an interface. Turns a request into one question at a time, a short set of approaches, and a written design approved in sections.
---

# Design spec

Kit piece: the design-spec template and the spec-review prompt. Path: architectural (bounded
changes get a short in-chat design instead; spikes get a probe).

## Procedure

1. Ask one question per message. Prefer multiple choice. Stop asking when you can state the
   purpose, the constraints, and what success looks like.
2. Write back your understanding in a few lines, separating what the user said from what you
   assumed. Wait for a correction.
3. Propose two or three approaches. Lead with your recommendation and say why. Remove any
   feature that is not needed for the stated success criteria.
4. Present the design in sections sized to their complexity. After each section, ask whether it
   is right. Revise the section before moving on.
5. Save the approved design to `docs/specs/YYYY-MM-DD-<topic>.md` using the template below.
6. Run the spec-review prompt (below) on the saved file, fix what it finds, then ask the user to
   review the file. Do not start a plan until the file is approved.

## Template

    # <Topic> design
    ## Purpose and success criteria
    ## Constraints (what must not change)
    ## Approach chosen, and the two rejected (one line each, with the reason)
    ## Components and their interfaces (inputs, outputs, what each depends on)
    ## Data flow
    ## Errors and their handling
    ## Testing: what each interface test proves
    ## Out of scope

## Spec-review prompt

Give a fresh reader only the file. Ask them to list, without fixing anything:

- every placeholder, TBD, or sentence that would need a decision to implement;
- every pair of sentences that contradict each other;
- every requirement that two engineers could implement differently;
- every feature not required by the success criteria.

The author fixes each item. The reviewer does not see the conversation.

## Cost of skipping this

Code written against an unstated design is judged against the code's author's memory. The first
review then argues about intent instead of evidence, and the spec is reconstructed after the
fact to match what was built.
