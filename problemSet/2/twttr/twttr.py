def main():
    text = input("Input: ")
    text_shorter = shorten(text)
    print("Output:", text_shorter)


def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    txt = ""
    for character in text:
        for vowel in vowels:
            if character.lower() == vowel:
                character = ""
        txt = txt + character
    return txt


if __name__ == "__main__":
    main()