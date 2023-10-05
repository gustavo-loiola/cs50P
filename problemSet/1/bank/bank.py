def main():
    greeting = input("Greeting: ").strip().lower()

    if starts_h(greeting):
        match first_word(greeting):
            case "hello" | "hello,":
                print("$0")
            case _:
                print("$20")

    else:
        print("$100")

def starts_h(a):
    return a[0] == "h"

def first_word(a):
    a = a.split()
    return a[0]

main()