# Refueling

import fuel

import pytest


def test_string():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")


def test_float():
    with pytest.raises(ValueError):
        fuel.convert("1.5/3")


def test_integer():
    assert fuel.convert("3/4") == 75
    assert fuel.gauge(75) == "75%"


def test_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("0/0")


def test_x_greater_than_y():
    with pytest.raises(ValueError):
        fuel.convert("5/4")


def test_empty():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"


def test_full():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
