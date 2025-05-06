# Fuel Gauge

import sys


def main():
    """
    Prompts the user for a fraction, formatted as X/Y, wherein each of
    X and Y is an integer, and then outputs, as a percentage rounded to
    the nearest integer, how much fuel is in the tank. If, though, 1% or
    less remains, output E instead to indicate that the tank is essentially
    empty. And if 99% or more remains, output F instead to indicate that
    the tank is essentially full
    """
    while True:
        try:
            percentage = convert(input("Fraction: "))

            sys.exit(gauge(percentage))

        except (ValueError, ZeroDivisionError):
            ...


def convert(fraction: str) -> int:
    x, y = fraction.split("/")

    if int(x) > int(y):
        raise ValueError

    return int(x) * 100 / int(y)


def gauge(percentage: int) -> str:
    if 1 >= percentage:
        return "E"

    if 99 <= percentage:
        return "F"

    return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
