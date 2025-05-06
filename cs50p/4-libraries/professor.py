# Little Professor

import random


def main():
    answer = problems_solved = 0

    # Prompts the user for a level, 'n'.
    level = get_level()

    # Randomly generates ten (10) math problems formatted as 'X + Y = ',
    # wherein each of 'X' and 'Y' is a non-negative integer with 'n'digits.
    for _ in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)

        # Prompts the user to solve each of those problems.

        # If an answer is not correct (or not even a number), the program
        # should output EEE and prompt the user again, allowing the user
        # up to three tries in total for that problem.

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == x + y:
                    problems_solved += 1
                    break

                raise ValueError

            except ValueError:
                print("EEE")

        # If the user has still not answered correctly after three tries,
        # the program should output the correct answer.
        else:
            if answer != x + y:
                print(f"{x} + {y} = {x+y}")

    # The program should ultimately output the user’s score, the number
    # of correct answers out of 10.
    print(f"Score: {problems_solved}")


def get_level():
    try:
        level = int(input("Level: "))

        # If the user does not input 1, 2, or 3, the program should
        # prompt again.
        return level if level in range(1, 4) else get_level()

    except ValueError:
        return get_level()


def generate_integer(level):
    # Edge-case because 10(0) is 1, not 0.
    if level == 1:
        return random.randint(0, 9)

    return random.randint(10 ** (level - 1), 10**level - 1)


if __name__ == "__main__":
    main()
