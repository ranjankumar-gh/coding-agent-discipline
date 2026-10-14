# coding-agent-discipline

Companion code for *Discipline for Coding Agents* by Ranjan Kumar.

The book's running example is **flowround**, a Python library that parses, edits, and serializes
Mermaid flowcharts under a byte-for-byte round-trip invariant:

    serialize(parse(x)) == x

The repository is built ship by ship. Each chapter that prints package code has a `wip/<chapter>`
tag, and the final chapter tags are cut at release. The design of each ship is in `docs/`.

## Run the tests

    python -m venv .venv
    .venv/bin/pip install -e ".[dev]"      # Windows: .venv\Scripts\pip install -e ".[dev]"
    .venv/bin/pytest

## License

MIT. See `LICENSE`.
