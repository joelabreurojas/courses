# Just setting up my twttr


def main() -> None:
    """
    Prompts the user for a str of text and then outputs that same text
    but with all vowels (A, E, I, O, and U) omitted, whether inputted in
    uppercase or lowercase
    """

    text: str = ""

    for char in input("Input: "):
        if char.lower() not in "aeiou":
            text += char

    print("Output:", text)


if __name__ == "__main__":
    main()
