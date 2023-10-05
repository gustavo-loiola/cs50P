import sys


def main():
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    with open(get_file("py")) as file:
        for line in file:
            if line.isspace():
                blank_lines += 1
            elif line.lstrip()[0] == "#":
                comment_lines += 1
            else:
                code_lines += 1
    print(code_lines)


def get_file(format_sufix):
    common_suffixes = {"py": "Python", "pdf": "pdf", "csv": "csv", "c": "c"}

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]
        format = file.rsplit(".")[-1]

        if len(format) == 2 and format == format_sufix and file_open(file):
            return file
        else:
            sys.exit(f"Not a {common_suffixes[format_sufix]} file")


def file_open(file):
    try:
        with open(file):
            return True
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
