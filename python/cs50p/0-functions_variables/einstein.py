# Einstein


def main():
    """
    Prompts the user for mass as an integer (in kilograms) and then outputs the
    equivalent number of Joules as an integer.
    Assume that the user will input an integer.
    """
    print("E:", joules(int(input("m: "))))


def joules(mass):
    return mass * 300000000**2  # E = mc^2


main()
