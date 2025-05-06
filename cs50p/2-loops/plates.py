# Vanity Plates


def main():
    """
    Prompts the user for a vanity plate and then output Valid if meets all
    of the requirements or Invalid if it does not. Assume that any letters
    in the user’s input will be uppercase
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Returns True if s meets all requirements and False if it does
    not. Assume that s will be a str. You’re welcome to implement additional
    functions for is_valid to call (e.g., one function per requirement)
    """
    if not s.isalnum():
        return False

    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha():
        return False

    end = ""

    for char in s[2:]:
        if char.isnumeric():
            end += char

    if end and end[0] == "0":
        return False

    if not s.endswith(end):
        return False

    return True


main()
