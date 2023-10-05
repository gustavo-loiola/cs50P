def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    # will repeat until get the number
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            # don't specify the error, but is a bit more user friendly
            pass


main()
