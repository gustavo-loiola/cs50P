def main():
    names = get_name("Name: ")
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print("Adieu, adieu, to", end=" ")
        for name in names:
            if name != names[-1]:
                print(name, end=", ")
            else:
                print(f"and {name}")


def get_name(prompt):
    list_names = []
    while True:
        try:
            name = input(prompt)
            list_names.append(name)
        except EOFError:
            return list_names


main()
