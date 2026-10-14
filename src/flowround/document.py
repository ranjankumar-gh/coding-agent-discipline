"""Lossless line model for the flowround subset.

Ship 0: parse and serialize only. Every input string round-trips byte for byte:
``parse(x).serialize() == x``. Each line keeps its exact text and its exact line
ending, so nothing the parser does not interpret can be lost.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_HEADER = re.compile(r"flowchart (TD|TB|LR|RL|BT)\s*")
_NODE = re.compile(r"\s*[A-Za-z][A-Za-z0-9_]*\[[^\]]*\]\s*")
_ENDPOINT = r"[A-Za-z][A-Za-z0-9_]*(?:\[[^\]]*\])?"
_EDGE = re.compile(rf"\s*{_ENDPOINT}\s*-->(?:\|[^|]*\|)?\s*{_ENDPOINT}\s*")
_COMMENT = re.compile(r"\s*%%.*")
_BLANK = re.compile(r"\s*")


@dataclass(frozen=True)
class Line:
    """One source line: its text without the line ending, the ending, and its kind."""

    text: str
    ending: str  # "\n", "\r\n", or "" for an unterminated final line
    kind: str  # header | node | edge | comment | blank | other


@dataclass(frozen=True)
class Document:
    """A parsed flowchart. ``serialize()`` reproduces the source exactly."""

    lines: tuple[Line, ...]

    def serialize(self) -> str:
        return "".join(line.text + line.ending for line in self.lines)

    def of_kind(self, kind: str) -> tuple[Line, ...]:
        return tuple(line for line in self.lines if line.kind == kind)


def _classify(text: str) -> str:
    for kind, pattern in (
        ("header", _HEADER),
        ("node", _NODE),
        ("edge", _EDGE),
        ("comment", _COMMENT),
        ("blank", _BLANK),
    ):
        if pattern.fullmatch(text):
            return kind
    return "other"


def parse(source: str) -> Document:
    """Parse ``source`` into a Document. Never raises; unknown lines are kept as ``other``."""
    pieces = source.split("\n")
    lines: list[Line] = []
    for index, piece in enumerate(pieces):
        last = index == len(pieces) - 1
        if last and piece == "":
            break  # the text ended with a newline (or was empty): no further line
        text, ending = piece, ("" if last else "\n")
        if not last and text.endswith("\r"):
            text, ending = text[:-1], "\r\n"
        lines.append(Line(text=text, ending=ending, kind=_classify(text)))
    return Document(lines=tuple(lines))
