# Just setting up my twttr


def main() -> None:
    """
    Prompts the user for a str of text and then outputs that same text
    but with all vowels (A, E, I, O, and U) omitted, whether inputted in
    uppercase or lowercase
    """

    print("Output:", shorten(input("Input: ")))


def shorten(word: str) -> str:
    return "".join(char for char in word if char.lower() not in "aeiou")


if __name__ == "__main__":
    main()
