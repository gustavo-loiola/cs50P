def main():
    fraction = get_fraction("Fraction: ")
    fuel_condition = convert(fraction)
    print(fuel_condition)


def get_fraction(prompt):
    while True:
        try:
            fraction_characters = input(prompt).partition("/")
            x = int(fraction_characters[0])
            y = int(fraction_characters[-1])
            if x > y:
                pass
            else:
                return x / y
        except ZeroDivisionError and ValueError:   #could've used except(ValueError, ZeroDivisionError)
            pass


def convert(n):
    percentage = round(n * 100)
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


main()
