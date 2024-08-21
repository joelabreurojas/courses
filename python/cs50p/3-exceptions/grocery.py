# Grocery List


def main() -> None:
    """
    Prompts the user for items, one per line, until the user inputs control-d
    (which is a common way of ending one’s input to a program). Then output
    the user’s grocery list in all uppercase, sorted alphabetically by
    item, prefixing each line with the number of times the user inputted
    that item. No need to pluralize the items. Treat the user’s input
    case-insensitively.
    """
    try:
        list = {}
        while True:
            item = input().strip().upper()

            if item not in list:
                list[item] = 1
            else:
                list[item] -= -1  # list[item] += 1

    except EOFError:
        for keys, values in sorted(list.items()):
            print(values, keys)


if __name__ == "__main__":
    main()
