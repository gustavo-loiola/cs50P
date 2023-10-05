import csv
import sys


def main():
    exist, new = get_files("csv", 2)
    students = []

    with open(exist) as exist:
        reader = csv.DictReader(exist)
        for row in reader:
            name = row["name"].split(", ")
            students.append({"first": name[1], "last": name[0], "house": row["house"]})

    with open(new, "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=list(students[0]))
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def get_files(sufix, amount_arg):
    if len(sys.argv) < amount_arg + 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > amount_arg + 1:
        sys.exit("Too many command-line arguments")
    else:
        for file in sys.argv[1:]:
            file_words = file.rsplit(".")
            file_format = file_words[-1]

            if file_format == sufix and len(file_words) == 2 and file_opens(file):
                pass
            else:
                sys.exit(f"Not a {sufix.upper} file")

        return sys.argv[1:]


def file_opens(file):
    if file == sys.argv[-1]:
        return True
    try:
        with open(file):
            return True
    except FileNotFoundError:
        sys.exit(f"Could not read {file}")


if __name__ == "__main__":
    main()
