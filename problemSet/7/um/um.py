import re


def main():
    print(count(input("Text: ")))


def count(s):
    if find := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(find)
    else:
        return 0


if __name__ == "__main__":
    main()
