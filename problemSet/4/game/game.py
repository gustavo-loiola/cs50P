import random
import sys


def main():
    level = get_level("Level: ")
    n = random.randint(1, level)

    while True:
        guess = get_guess("Guess: ")
        situation, correct = verify(n, guess)

        if correct:
            print(situation)
            # break
            sys.exit()
        else:
            print(situation)


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
            else:
                pass
        except ValueError:
            pass


def get_guess(prompt):
    while True:
        try:
            guess = int(input(prompt))
            if guess > 0:
                return guess
            else:
                pass
        except ValueError:
            pass


def verify(n, guess):
    if guess < n:
        return "Too small!", False
    elif guess > n:
        return "Too large!", False
    else:
        return "Just right!", True

if __name__ = "__main__":
    main()
