# Fuel Gauge


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
            x, y = input("Fraction: ").split("/")

            if int(x) > int(y):
                continue

            fuel = int(x) * 100 / int(y)

            if 1 >= fuel:
                print("E")
            elif 99 <= fuel:
                print("F")
            else:
                print(f"{round(fuel)}%")

            break

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
