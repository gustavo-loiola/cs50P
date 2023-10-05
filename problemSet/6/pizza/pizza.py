import sys
import csv

from os.path import splitext
from tabulate import tabulate


def main():
    sufix = [".csv"]
    menus = ["regular.csv", "sicilian.csv"]
    menu = get_file(sufix, 1)[0]

    if menu in menus:
        table = convert_table(menu)  # table is a list of lists and each list is a row.csv
        print(tabulate(table, headers="firstrow", tablefmt="grid"))


def get_file(sufix, amount_arg):
    check_len(amount_arg)
    for file in sys.argv[1:]:
        if check_format(sufix, file) and file_opens(file):
            pass
        else:
            sys.exit(f"Not a {sufix[0].lstrip('.').upper()} file")

    return sys.argv[1:]


def file_opens(file):
    try:
        with open(file):
            return True
    except FileNotFoundError:
        sys.exit(f"Could not read {file}")


def check_len(amount_arg):
    if len(sys.argv) < amount_arg + 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > amount_arg + 1:
        sys.exit("Too many command-line arguments")
    else:
        pass


def check_format(format_list, file):
    file = splitext(file)
    if file[1] in format_list:
        return True
    else:
        return False


def convert_table(file):
    table = []

    with open(file) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        return table


if __name__ == "__main__":
    main()
