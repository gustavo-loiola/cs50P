def main():
    camel_case = input("camelCase: ")
    snake_case = make_snake(camel_case)
    print("snake_case:", snake_case)

def make_snake(words):
    snake_case = ""
    for character in words:
        capitalized = character.isupper()
        if capitalized:
            snake_case = snake_case + "_" + character.lower()
        else:
            snake_case = snake_case + character

    return snake_case

main()