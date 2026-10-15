# flowround specification

## Purpose

flowround parses, edits, and serializes a subset of Mermaid flowchart syntax. Its one
non-negotiable property is the round-trip invariant:

    serialize(parse(x)) == x        for every input string x

The invariant gives every gate in the book a real oracle: a change that alters bytes the
user did not ask to change has failed, whatever the tests say about the edit itself.

## Grammar subset

| Line kind | Form | Example |
|---|---|---|
| header | `flowchart` followed by TD, TB, LR, RL, or BT | `flowchart TD` |
| node | identifier, `[`, label without `]`, `]` | `A[Receive order]` |
| edge | endpoint, `-->`, optional `\|label\|`, endpoint; an endpoint is an identifier, optionally followed by `[label]` | `B -->\|valid\| C`, `A[Receive order] --> B[Validate]` |
| comment | `%%` to end of line | `%% orders service` |
| blank | whitespace only | |
| other | anything else | kept verbatim, not interpreted |

Ship 0 classifies lines; it does not validate them. An `other` line is preserved exactly.

## Line endings and edges of the text

- Line endings are `\n` or `\r\n`, and each line keeps its own ending.
- A final line may lack an ending.
- A lone `\r` is part of the text, not a line ending.
- Characters such as U+2028 and U+0085 are text, not line breaks.
- Empty input is a valid document with no lines.

## Ship 0: parse and serialize

`parse` splits the text on `\n`, keeps each line's exact text and ending, and classifies each
line. `serialize` concatenates them. Because nothing is discarded or normalized, the invariant
holds for every input, including ones the grammar does not cover.

## Planned edit operations (ship 1)

Rename a node; add a node; add an edge; relabel an edge. Each operation must keep the
invariant: the bytes outside the edited line are unchanged, and the edited line's ending is
unchanged.

One exception, for appending. A line cannot be followed by another line without a line ending,
so an operation that appends a line after an unterminated final line must give that line the
document's dominant ending. The final line's text does not change; only its ending is set. The
appended line is then unterminated, so the file still ends without a newline. `add_edge` is the only
operation this applies to.

## The regex-splice trap

The obvious edit is a regex replacement over the whole text, such as replacing `A\[` with
`X[` everywhere. It changes bytes the user did not mean to touch: the same pattern inside a
comment, inside a label, or across a `\r\n` boundary. The round-trip check fails on those edits
even when the intended change looks right. flowround forbids whole-text splicing: every edit goes
through the line model, which owns each line's exact bytes.
