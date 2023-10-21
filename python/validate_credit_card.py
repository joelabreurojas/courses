from typing import Final, List
from sys import exit

LENGTH: Final[int] = 16


def main() -> None:
    card_numbers: List[int] = get_input()

    if not luhn_algorithm(card_numbers):
        print('INVALID')
        exit(1)

    print('VALID')
    exit(0)


def get_input() -> int:
    while True:
        try:
            numbers: List[int] = [
                int(number) for number in input('Number (16 digits): ')
            ]
        except ValueError:
            print('Not an integer.')
        else:
            if numbers and len(numbers) == LENGTH:
                return numbers


def luhn_algorithm(numbers: List[int]) -> bool:
    addition: int = 0
    product: int = 0

    for i in range(0, LENGTH, 2):
        if (product := numbers[i] * 2) > 9:
            product -= 9

        addition += product + numbers[i + 1]

    return not addition % 10


if __name__ == '__main__':
    main()
