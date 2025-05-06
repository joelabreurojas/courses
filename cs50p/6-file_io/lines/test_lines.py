from lines import check_arguments, check_extension, check_existence, count_lines
import pytest


def test_arguments() -> None:
    with pytest.raises(ValueError):
        check_arguments(["python"])

    with pytest.raises(ValueError):
        check_arguments(["python", "foo", "bar"])


def test_extension() -> None:
    with pytest.raises(ValueError):
        check_extension("foo.notpy")


def test_existence() -> None:
    with pytest.raises(FileNotFoundError):
        check_existence("foo.py")


def test_counter() -> None:
    assert count_lines("lines.py") == 35
