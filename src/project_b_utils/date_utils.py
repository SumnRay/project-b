"""Utilities for working with dates."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Union


DateLike = Union[date, datetime, str]


def _to_date(value: DateLike) -> date:
    """
    Convert a supported value to datetime.date.

    Strings must use ISO format: YYYY-MM-DD.
    """

    if isinstance(value, datetime):
        return value.date()

    if isinstance(value, date):
        return value

    if isinstance(value, str):
        return date.fromisoformat(value)

    raise TypeError(
        "value must be date, datetime or ISO date string"
    )


def get_current_date() -> str:
    """
    Return the current local date in ISO format.
    """

    return date.today().isoformat()


def format_date(
    value: DateLike,
    output_format: str = "%d.%m.%Y",
) -> str:
    """
    Format a date using datetime.strftime syntax.
    """

    return _to_date(value).strftime(output_format)


def add_days(
    value: DateLike,
    days: int,
) -> str:
    """
    Add days to a date and return the result
    in ISO format.
    """

    return (
        _to_date(value)
        + timedelta(days=days)
    ).isoformat()


def days_between(
    start: DateLike,
    end: DateLike,
) -> int:
    """
    Return the signed number of days
    between two dates.
    """

    return (
        _to_date(end)
        - _to_date(start)
    ).days