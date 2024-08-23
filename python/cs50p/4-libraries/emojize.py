# Emojize

from emoji import emojize


def main():
    """
    Prompts the user for a str in English and then outputs the 'emojized'
    version of that str, converting any codes (or aliases) therein to their
    corresponding emoji.
    """
    print("Output: " + emojize(input("Input: "), language="alias"))


if __name__ == "__main__":
    main()
