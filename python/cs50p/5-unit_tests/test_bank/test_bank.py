# Back to the Bank

from bank import value


def test_hello_greetings():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_greetings_starting_with_h():
    assert value("hi") == 20
    assert value("HEY") == 20


def test_other_greetings():
    assert value("What's up?") == 100
