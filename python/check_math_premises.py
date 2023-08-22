import re
from typing import List


def check_mathematical_premises(premises: str) -> None:
    premises_list: List[str] = premises.split(", ")

    operand: str = "[ ]*[a-zA-Z0-9]+[ ]*"
    operator: str = "[ ]*([+-/*%<>]|[*][*]|[/][/]|[=<>!][=])[ ]*"
    regex: str = f"^{operand}[=]{operand}{operator}{operand}$"

    for premise in premises_list:
        status: str = "acepted" if bool(re.search(regex, premise)) else "wrong"
        print(f"{premise:<30}{status} format")


if __name__ == "__main__":
    mathematical_premises: str = ""

    mathematical_premises = "anything=a+b-c-d-e-f-g-h-i, b = 1 <= 10"
    check_mathematical_premises(mathematical_premises)

    mathematical_premises = "213 = 2 * * 23, 1 = 2 3, c = 37, d = 2 > 1"
    check_mathematical_premises(mathematical_premises)
