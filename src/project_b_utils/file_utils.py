"""Small UTF-8 text-file helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Union


PathLike = Union[str, Path]


def write_text(
    path: PathLike,
    content: str,
) -> Path:
    """
    Write UTF-8 text to a file.

    Parent directories are created automatically.
    """

    target = Path(path)

    target.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    target.write_text(
        content,
        encoding="utf-8",
    )

    return target


def read_text(path: PathLike) -> str:
    """
    Read UTF-8 text from a file.
    """

    return Path(path).read_text(
        encoding="utf-8",
    )


def count_lines(path: PathLike) -> int:
    """
    Count lines in a UTF-8 text file.
    """

    text = read_text(path)

    if not text:
        return 0

    return len(text.splitlines())