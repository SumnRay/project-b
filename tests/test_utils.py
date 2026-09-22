from datetime import date

from project_b_utils import (
    capitalize_words,
    format_date,
    reverse_string,
)


def test_format_date():
    result = format_date(date(2026, 9, 22))

    assert result == "22.09.2026"


def test_reverse_string():
    result = reverse_string("Hello")

    assert result == "olleH"


def test_capitalize_words():
    result = capitalize_words("hello world from project b")

    assert result == "Hello World From Project B"