def main() -> None:
    size: int = get_size()

    for row in range(size):

        # Draw spaces
        print(' ' * (size - row - 1), end='')

        # Draw blocks
        print('#' * row, end='')
        print('#', end='')  # This is the center block
        print('#' * row)


def get_size() -> int:
    size: int = 0

    while size < 1 or size > 9:
        try:
            size = int(input('Size (3-9): '))
        except ValueError:
            print('Not an integer')

    return size


if __name__ == '__main__':
    main()
