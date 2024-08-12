# Math Interpreter


def main():
    """
    Prompts the user for an arithmetic expression and then calculates and
    outputs the result as a floating-point value formatted to one decimal place.
    """

    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    match y:
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))
        case _:
            print("Invalid operator")


main()
