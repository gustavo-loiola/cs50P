import emoji


def main():
    s = input("Input: ")
    print(emoji.emojize(s, language="alias"))


main()
