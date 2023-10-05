def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lstrip().lower().split(" ", maxsplit=1)
    if greeting[0][0] != "h":
        return 100
    else:
        if greeting[0][0:5] == "hello":
            return 0
        else:
            return 20


if __name__ == "__main__":
    main()
