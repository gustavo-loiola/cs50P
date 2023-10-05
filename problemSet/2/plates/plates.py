def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not(verify1(s)):
        return False
    elif not(verify2(s)):
        return False
    elif not(verify3(s)):
        return False
    elif not(verify4(s)):
        return False
    else:
        return True

def verify1(s):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for character in s[0:2]:
        for number in numbers:
            if character == number:
                return False
    return True

def verify2(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def verify3(s):
    not_allowed = [",", " ", "!", "?", ".", ":", ";"]
    for character in s:
        for restriction in not_allowed:
            if character == restriction:
                return False
    return True

def verify4(s):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    last_character = ""
    for character in s:
        if not(character.isnumeric()) and last_character.isnumeric():
            return False
        elif character == "0" and not(last_character.isnumeric()):
            return False
        else:
            last_character = character
    return True

main()