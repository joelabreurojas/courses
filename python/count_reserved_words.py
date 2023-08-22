import re
from collections import Counter
from keyword import kwlist
from typing import List


def count_keywords(words: str, keywords: str) -> None:
    words_list: List[str] = re.sub("([^a-zA-Z])", " ", words).split()
    keyword_list: List[str] = keywords.split(", ")

    counted_words: Counter[str] = Counter(words_list)

    for keyword in keyword_list:
        ocurrences: int = (counted_words)[keyword]
        if ocurrences:
            print(f"{keyword :<10}{ocurrences}")


if __name__ == "__main__":
    code: str = "if True: print(None)"
    reserved_keywords: str = ", ".join(kwlist)

    count_keywords(code, reserved_keywords)
