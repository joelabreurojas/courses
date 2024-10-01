# Lines of Code

import os
import sys


def main() -> None:
    """
    Expects exactly one command-line argument, the name (or path) of a Python
    file, and outputs the number of lines of code in that file, excluding
    comments and blank lines. If the user does not specify exactly one
    command-line argument, or if the specified file’s name does not end
    in `.py`, or if the specified file does not exist, the program should
    instead exit via `sys.exit`.
    """

    check_arguments(sys.argv)
    check_extension(sys.argv[1])
    check_existence(sys.argv[1])

    print(count_lines(sys.argv[1]))


def check_arguments(args: list[str]) -> None:
    if len(args) < 2:
        raise ValueError("Too few command-line arguments")

    if len(args) != 2:
        raise ValueError("Too many command-line arguments")


def check_extension(filename: str) -> None:
    if not filename.endswith(".py"):
        raise ValueError("Not a Python file")


def check_existence(filename: str) -> None:
    if not os.path.exists(filename):
        raise FileNotFoundError("File does not exist")


def count_lines(filename: str) -> int:
    count: int = 0

    with open(filename) as file:
        for line in file:
            if not line.isspace() and not line.lstrip().startswith("#"):
                count += 1

    return count


if __name__ == "__main__":
    main()
