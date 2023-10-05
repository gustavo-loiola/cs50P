from datetime import date, timedelta
import sys, re, inflect


def main():
    print(convert(input("Date of Birth: ")))


def convert(date):
    date = validate_format(date)
    min = str(int(round((timedelta.total_seconds(date.today() - date)) / 60, 0)))
    return (inflect.engine().number_to_words(min, andword="") + " minutes").capitalize()


def validate_format(d):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", d, re.ASCII):
        try:
            date_obj = date(int(matches[1]), int(matches[2]), int(matches[3]))
            return date_obj
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
