import sys


def main():
    percentage = convert(input("Fraction: "))
    fuel = gauge(percentage)
    print(fuel)


def convert(fraction_str):
    """'
    try:
        fraction_characters = fraction_str.partition("/")
        x = int(fraction_characters[0])
        y = int(fraction_characters[-1])
    except ValueError:
        assert ValueError
        sys.exit()

    try:
        if x > y:
            raise ValueError
        else:
            return round((x / y) * 100)
    except ZeroDivisionError:
        assert ZeroDivisionError
    """
    fraction_characters = fraction_str.partition("/")
    try:
        x = int(fraction_characters[0])
        y = int(fraction_characters[-1])
        if x > y and y != 0:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        else:
            return round((x / y) * 100)

    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
