def main():
    s = input()
    print(convert(s))


def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()