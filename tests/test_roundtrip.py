"""Ship 0 invariant: parse(x).serialize() == x for every input x."""

import random

import pytest

from flowkit import parse

SAMPLE = (
    "flowchart TD\n"
    "%% orders service\n"
    "A[Receive order] --> B[Validate]\n"
    "B -->|valid| C[Charge]\n"
    "\n"
    "C --> D[Ship]\n"
)

FIXED_CASES = {
    "empty": "",
    "single line, no newline": "flowchart TD",
    "single line, newline": "flowchart TD\n",
    "sample": SAMPLE,
    "crlf endings": SAMPLE.replace("\n", "\r\n"),
    "mixed endings": "flowchart LR\r\nA[x] --> B[y]\nB --> C[z]\r\n",
    "no final newline": SAMPLE.rstrip("\n"),
    "trailing spaces": "flowchart TD   \nA[x]   \n",
    "lone carriage return at end": "flowchart TD\r",
    "carriage return run": "A[x]\r\r\nB[y]\n",
    "unicode labels": "flowchart TD\nA[Café → résumé] --> B[名前]\n",
    "only blank lines": "\n\n\n",
    "unsupported syntax kept": "flowchart TD\nclassDef hot fill:#f00\nA:::hot --> B\n",
}


@pytest.mark.parametrize("source", FIXED_CASES.values(), ids=FIXED_CASES.keys())
def test_fixed_cases_round_trip(source: str) -> None:
    assert parse(source).serialize() == source


def test_random_strings_round_trip() -> None:
    # Characters that matter to the line model, plus ones that str.splitlines() would split on.
    alphabet = list("AB[]()|%- >\r\n\t") + ["\x0b", "\x0c", "\x85", " ", " ", "é"]
    rng = random.Random(0)  # fixed seed: the same 2000 inputs every run
    for _ in range(2000):
        source = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 60)))
        assert parse(source).serialize() == source, repr(source)


def test_kinds_are_assigned() -> None:
    document = parse(SAMPLE)
    assert [line.kind for line in document.lines] == [
        "header",
        "comment",
        "edge",
        "edge",
        "blank",
        "edge",
    ]


def test_unknown_lines_are_kept_as_other() -> None:
    document = parse("flowchart TD\nclassDef hot fill:#f00\n")
    assert document.of_kind("other")[0].text == "classDef hot fill:#f00"
