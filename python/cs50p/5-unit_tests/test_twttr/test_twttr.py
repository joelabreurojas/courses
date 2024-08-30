from twttr import shorten


def test_lowercase_vowel_replacement() -> None:
    assert shorten("twitter") == "twttr"


def test_capitalized_vowel_replacement() -> None:
    assert shorten("TWITTER") == "TWTTR"


def test_omiting_numbers() -> None:
    assert shorten("1234567890") == "1234567890"


def test_omiting_punctuation() -> None:
    assert shorten("Hello, World!") == "Hll, Wrld!"
