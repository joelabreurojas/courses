# Bitcoin Price Index import

import sys
import requests


def main() -> None:
    """
    Expects the user to specify as a command-line argument the number of
    Bitcoins, that they would like to buy. If that argument cannot be converted
    to a float, the program should exit via sys.exit with an error message.

    Queries the API for the CoinDesk Bitcoin Price Index at
    'https://api.coindesk.com/v1/bpi/currentprice.json', which returns a JSON
    object, among whose nested keys is the current price of Bitcoin as a
    float. Be sure to catch any exceptions.

    Outputs the current cost of Bitcoins in USD to four decimal places,
    using , as a thousands separator.
    """

    try:
        if 2 > len(sys.argv):
            exit("Missing command-line argument")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        cost = response.json()["bpi"]["USD"]["rate_float"] * float(sys.argv[1])

        print(f"${cost:,.4f}")

    except ValueError:
        exit("Command-line argument is not a number")

    except requests.RequestException:
        exit("Server error")


if __name__ == "__main__":
    main()
