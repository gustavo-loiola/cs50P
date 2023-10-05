import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        i = 1
        while i <= 4:
            set = matches.group(i)
            if not in_range(set):
                return False
            else:
                i += 1

        return True
    else:
        return False


def in_range(n):
     try:
          n = int(n)
     except ValueError:
          return False

     if 0 <= n <= 255:
        return True
     else:
        return False


if __name__ == "__main__":
    main()
