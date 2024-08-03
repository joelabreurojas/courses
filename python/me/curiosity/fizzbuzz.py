def main() -> None:
    number: int = get_number()

    for i in range(1, number + 1):
        if i % 3 == 0:
            print('Fizz', end='')
        if i % 5 == 0:
            print('Buzz', end='')
        if (i % 3) != 0 != (i % 5):
            print(i, end='')

        print()


def get_number() -> int:
    while True:
        try:
            number: int = int(input('Number: '))
        except ValueError:
            print('Not an integer.')
        else:
            return number


if __name__ == "__main__":
    main()
