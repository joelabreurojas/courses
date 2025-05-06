# Meal Time


def main():
    """
    Prompts the user for a time and outputs whether it’s breakfast time, lunch
    time, or dinner time. If it’s not time for a meal, don’t output anything at
    all. Assume that the user’s input will be formatted in 24-hour time as
    #:## or ##:##. And assume that each meal’s time range is inclusive.
    For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between,
    it’s time for breakfast.
    """
    time = convert(input("What time is it? "))

    if 7.00 <= time <= 8.00:
        print("breakfast time")

    elif 12.00 <= time <= 13.00:
        print("lunch time")

    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    """
    Converts time, a str in 24-hour format, to the corresponding number of hours
    as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30
    minutes), convert should return 7.5 (i.e., 7.5 hours).
    """

    time = time.lower().strip()  # format
    hours, minutes = time.split(":")

    # Support for 12-hour times

    if minutes.endswith("a.m."):
        minutes = minutes.removesuffix(" a.m.")

    elif time.endswith("p.m."):
        minutes = minutes.removesuffix(" p.m.")
        hours = int(hours) + 12

    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
