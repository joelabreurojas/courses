from sys import argv


def main() -> None:
    if len(argv) != 2:
        name: str = input('What is your name? >')
        print(f"Hello, {name}")

    print(f'Hello, {argv[1]}')


if __name__ == '__main__':
    main()
