def main() -> None:
    size: int = get_size()

    for row in range(size):
        print_spaces(row, size)
        print('#', end='')
        print_blocks(row, True)


def get_size() -> int:
    size: int = 0

    while size < 1 or size > 9:
        try:
            size = int(input('Size (3-9): '))
        except ValueError:
            print('Not an integer')

    return size


def print_spaces(row: int, size: int) -> None:
    spaces: int = row - size + 1

    while spaces < 0:
        print(' ', end='')
        spaces += 1

    print_blocks(row, False)


def print_blocks(row: int, jump: bool) -> None:
    for _ in range(row):
        print('#', end='')

    if jump:
        print()


if __name__ == '__main__':
    main()
