# Home Federal Savings Bank


def main():
    # Prompts the user for a greeting.

    money = value(input("Greeting: "))

    print(f"${money}")


def value(greeting):
    """
    Expects a str as input and returns an int, namely 0 if that str starts with
    "hello", 20 if that str starts with an “h” (but not “hello”),
    or 100 otherwise, treating the str case-insensitively.
    """

    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0

    if greeting.startswith("h"):
        return 20

    return 100


if __name__ == "__main__":
    main()
