# Frank, Ian and Glen's Letters'

import random
import sys
from pyfiglet import Figlet


def main():
    """
    1. Expects zero or two command-line arguments.

        a. Zero if the user would like to output text in a random font.

        b. Two if the user would like to output text in a specific font,
        in which case the first of the two should be -f or --font, and the
        second of the two should be the name of the font.

    2. Prompts the user for a str of text.

    3. Outputs that text in the desired font.

    If the user provides two command-line arguments and the first is not -f
    or --font or the second is not the name of a font, the program should
    exit via sys.exit with an error message.
    """

    figlet = Figlet()
    figlet_fonts = figlet.getFonts()

    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3:
        if "-f" != sys.argv[1] and "--font" != sys.argv[1]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in figlet_fonts:
            sys.exit("Invalid usage")

    figlet_font = random.choice(figlet_fonts) if len(sys.argv) == 1 else sys.argv[2]

    figlet.setFont(font=figlet_font)

    print("Output:", figlet.renderText(input("Input: ")), sep="\n")


if __name__ == "__main__":
    main()
