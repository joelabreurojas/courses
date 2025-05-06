# Making Faces


def main():
    """
    Prompts the user for input, calls convert on that input, and prints the
    result. You’re welcome, but not required, to prompt the user explicitly,
    as by passing a str of your own as an argument to input. Be sure to call
    main at the bottom of your file.
    """
    print("Output:", convert(input("Enter a happy/sad face as string: ")))


def convert(face=":)"):
    """
    Accepts a str as input and returns that same input with any :) converted to
    🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁
    (otherwise known as a slightly frowning face). All other text should be
    returned unchanged.
    """
    return face.replace(":)", "🙂").replace(":(", "🙁")


main()
