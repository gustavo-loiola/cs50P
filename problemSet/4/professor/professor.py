import random


def main():
    n = get_level()
    problems = make_problems(10, n)  # dic key = equation.str ; value = result_int
    score = 0
    for problem in problems:
        i = 0
        while i != 3:
            print(problem, end=" ")
            try:
                answer = int(input())
                if answer == problems[problem]:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                i += 1
        if i == 3:
            print(problem, problems[problem], sep=" ")
    print("Score:", score)


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def make_problems(amount, level):
    i = 0
    problems = {}
    while i < amount:
        x = generate_integer(level)
        y = generate_integer(level)

        if f"{x} + {y} =" not in problems:
            problems[f"{x} + {y} ="] = x + y
            i += 1

    return problems


if __name__ == "__main__":
    main()
