# Guessing Game

import random
import sys


def get_positive_integer(message: str) -> int:
    try:
        num = int(input(message))

        # If the user does not input a positive integer, the program should
        # prompt again.
        return num if num > 0 else get_positive_integer(message)

    except ValueError:
        raise get_positive_integer(message)


def main() -> None:
    # Prompts the user for a level, "n".
    n = get_positive_integer("Level: ")

    # Randomly generates an integer between 1 and "n", inclusive, using the
    # random module.
    secret = random.randint(1, n)

    while True:
        # Prompts the user to guess that integer. If the guess is not a
        # positive integer, the program should prompt the user again.

        guess = get_positive_integer("Guess: ")

        # If the guess is smaller than that integer, the program should output
        # "Too small!" and prompt the user again.
        if guess < secret:
            print("Too small!")

        # If the guess is larger than that integer, the program should output
        # "Too large!" and prompt the user again.
        elif guess > secret:
            print("Too large!")

        # If the guess is the same as that integer, the program should output
        # "Just right!" and exit.
        else:
            sys.exit("Just right!")


if __name__ == "__main__":
    main()
