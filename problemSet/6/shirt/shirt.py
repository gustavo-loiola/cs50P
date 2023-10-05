import sys
from os.path import splitext

from PIL import Image, ImageOps


def main():
    sufixes = [".jpg", ".jpeg", ".png"]
    photo, photo_edited = get_files(sufixes, 2)

    file_opens("shirt.png")
    photo = Image.open(photo)
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(photo_edited)


def get_files(sufix, amount_arg):
    check_len(amount_arg)
    for file in sys.argv[1:]:
        if check_format(sufix, file) and file_opens(file):
            pass
        else:
            sys.exit(f"Not a {sufix.upper} file")
    check_samesufix()

    return sys.argv[1:]


def file_opens(file):
    if file == sys.argv[-1]:  # this if exists bcs the last file is not created yet
        return True
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


def check_samesufix():
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")
    else:
        pass
    """
    i = 1
    while i < len(sys.argv[1:]) - 1:
        prefix1 = splitext(sys.argv(i))
        prefix2 = splitext(sys.argv(i+1))
        if prefix1[1] != prefix2[1]:
            sys.exit("Input and output have different extensions")
        else:
            i += 1
    """


if __name__ == "__main__":
    main()
