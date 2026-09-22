"""Public API for project-b utility library."""

from .date_utils import add_days, days_between, format_date, get_current_date
from .file_utils import count_lines, read_text, write_text
from .logging_utils import get_logger
from .string_utils import (
    capitalize_words,
    normalize_whitespace,
    reverse_string,
    slugify,
)

__all__ = [
    "get_current_date",
    "format_date",
    "add_days",
    "days_between",
    "reverse_string",
    "capitalize_words",
    "normalize_whitespace",
    "slugify",
    "read_text",
    "write_text",
    "count_lines",
    "get_logger",
]