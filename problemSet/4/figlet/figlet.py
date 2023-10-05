import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        # zero command-line arg
        s = input("Input: ")
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))
        print("Output: ")
        print(figlet.renderText(s))

    elif len(sys.argv) == 3:
        # two command-line arg
        if test_arg1(sys.argv[1]) and test_arg2(sys.argv[2]):
            figlet.setFont(font=sys.argv[2])
            s = input("Input: ")
            print("Output: ")
            print(figlet.renderText(s))

        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


def test_arg1(arg1):
    if arg1 == "-f" or arg1 == "--font":
        return True
    else:
        return False


def test_arg2(arg2):
    fonts = figlet.getFonts()
    if arg2 in fonts:
        return True
    else:
        return False

main()