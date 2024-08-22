# Outdated


def main():
    """
    Prompts the user for a date, anno Domini, in month-day-year order,
    formatted like 9/8/1636 or September 8, 1636. Then output that same date
    in YYYY-MM-DD format. If the user’s input is not a valid date in either
    format, prompt the user again. Assume that every month has no more than
    31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
    """

    MONTHS = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ")

        try:
            if "/" in date:
                month, day, year = date.split("/")
            elif ", " in date:
                month, day, year = date.split()
                month = MONTHS.index(month.title()) + 1
                day = day.strip(",")
            else:
                continue

            year = int(year)
            month = int(month)
            day = int(day)

            if 1 > year or 9999 < year:
                continue
            if 1 > month or 12 < month:
                continue
            if 1 > day or 31 < day:
                continue

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except EOFError:
            ...


if __name__ == "__main__":
    main()
