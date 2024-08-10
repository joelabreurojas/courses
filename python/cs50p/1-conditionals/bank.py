# Home Federal Savings Bank


def main():
    """
    Prompts the user for a greeting. If the greeting starts with “hello”,
    output $0. If the greeting starts with an “h” (but not “hello”), output $20.
    Otherwise, output $100. Ignore any leading whitespace in the user’s
    greeting, and treat the user’s greeting case-insensitively.
    """
    greeting = input("Greeting: ").lower().strip()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
