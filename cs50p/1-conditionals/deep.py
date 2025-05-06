# Deep Thought


def main():
    """
    Prompts the user for the answer to the Great Question of Life, the Universe
    and Everything, outputting Yes if the user inputs 42 or (case-insensitively)
    forty-two or forty two. Otherwise output No.
    """
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, "
        "and Everything? "
    )

    answer = answer.lower().strip()  # case-insensitively and remove whitespace

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")


main()
