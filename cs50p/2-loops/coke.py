# Coke Machine


def main() -> None:
    """
    Prompts the user to insert a coin, one at a time, each time informing
    the user of the amount due. Once the user has inputted at least
    50 cents, output how many cents in change the user is owed. Assume
    that the user will only input integers, and ignore any integer that
    isn’t an accepted denomination.
    """

    amount = 50

    while True:
        coin = int(input("Insert Coin: "))

        if coin in [50, 25, 10, 5, 1]:
            amount -= coin

        if amount <= 0:
            print(f"Change Owed: {abs(amount)}")
            break

        print(f"Amount Due: {amount}")


if __name__ == "__main__":
    main()
