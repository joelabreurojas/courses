# Re-requesting a Vanity Plate

from plates import is_valid


def test_not_alphanumeric():
    assert not is_valid("AA!!")


def test_start_with_two_letters():
    assert not is_valid("50")


def test_length():
    assert not is_valid("H")
    assert not is_valid("OUTATIME")


def test_numbers_in_middle():
    assert not is_valid("CS5O")


def test_zero_as_first_number():
    assert not is_valid("CS05")
