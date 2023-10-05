import requests
import json
import sys


def main():
    n = check_commandline()  # number of bitcoins
    price = n * bitcoin_price()  # cost in USD to buy n bitcoins
    print(f"${price:,.4f}")


def check_commandline():
    if len(sys.argv) < 2:
        sys.exit("Missing commnad-line argument")
    else:
        try:
            n = float(sys.argv[1])
            return n
        except ValueError:
            sys.exit("Command-line argument is not a number")


def bitcoin_price():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        currency = "USD"  # USD or GBP or EUR
        a = requests.get(url).json()
        return a["bpi"][currency]["rate_float"]
    except requests.RequestException:
        sys.exit()


if __name__ == "__main__":
    main()
