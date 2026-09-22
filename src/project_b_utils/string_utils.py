"""Utilities for working with strings."""

from __future__ import annotations

import re


def reverse_string(value: str) -> str:
    """
    Return value in reverse order.
    """

    return value[::-1]


def capitalize_words(value: str) -> str:
    """
    Capitalize each word in value.
    """

    return value.title()


def normalize_whitespace(value: str) -> str:
    """
    Replace consecutive whitespace
    with single spaces.
    """

    return " ".join(value.split())


def slugify(value: str) -> str:
    """
    Convert a string to a simple slug.
    """

    normalized = normalize_whitespace(value).lower()

    normalized = re.sub(
        r"[^\w\s-]",
        "",
        normalized,
        flags=re.UNICODE,
    )

    normalized = re.sub(
        r"[-\s]+",
        "-",
        normalized,
    )

    return normalized.strip("-")