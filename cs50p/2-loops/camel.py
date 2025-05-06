# camelCase


def main() -> None:
    """
    Prompts the user for the name of a variable in camel case and outputs the
    corresponding name in snake case. Assume that the user’s input will indeed
    be in camel case.

    """
    name = input("camelCase: ").strip()

    for char in name:
        if char.isupper():
            print("_", char.lower(), sep="", end="")
        else:
            print(char, end="")


if __name__ == "__main__":
    main()
