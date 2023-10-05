import validators


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(s):
    try:
        if validators.email(s):
            return "Valid"
        else:
            return "Invalid"
    except ValidationFailure:
        return "Invalid"


if __name__ == "__main__":
    main()
