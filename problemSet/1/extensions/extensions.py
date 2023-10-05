def main():
    file = input("File name: ").strip().lower()

    match suffixe(file):
        case "gif" | "png":
            print("image/", suffixe(file), sep = "")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print("application/", suffixe(file), sep = "")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


def suffixe(a):
    strpartition = a.rpartition(".")
    return strpartition[-1]


main()