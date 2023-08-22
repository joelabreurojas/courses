import re
from typing import List


def count_numbers_with_format(numbers: str) -> int:
    numbers_list: List[str] = numbers.split(", ")

    count: int = 0
    regex: str = "^[1-9][.][0-9]{4}$"

    for number in numbers_list:
        if re.search(regex, number):
            count -= -1

    return count


if __name__ == "__main__":
    real_numbers: str = "4.1111, 4, 123.234, 9.2222, 87.33334"

    counted_numbers: int = count_numbers_with_format(real_numbers)

    print(f"There are {counted_numbers} real numbers in the format a.bbbb")
