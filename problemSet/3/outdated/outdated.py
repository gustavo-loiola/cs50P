def main():
    # Receives a data1 or date2 and storages the date as a list like: ['day_str', 'month_str', 'year_str']
    date = get_date("Date: ")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    print(f"{year}-{month:02}-{day:02}")


def get_date(prompt):
    date = input(prompt).lstrip()
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if date[0] in numbers:
        # date2: month/day/year     XX/XX/XXXX
        while True:
            right_format, date2 = date2_type(date)
            if right_format:
                # verify month, day digits (1 to 31) and returns list
                conditions, date_list = date2_conditions(date2)
                if conditions:
                    return date_list
                else:
                    date = input(prompt)
            else:
                date = input(prompt)

    else:
        # date1: monthWritten day, year         August 9, 1938
        while True:
            # verify if is typed correctly
            right_format, date1 = date1_type(date)
            if right_format:
                conditions, date_list = date1_conditions(date1)
                if conditions:
                    return date_list
                else:
                    date = input(prompt)
            else:
                date = input(prompt)


def date1_type(date):
    date = date.split(" ")  # list: ["MonthWritten", "Day,", "Year"]
    # Verify comma
    try:
        day = date[1].index(",")
        return True, date
    except (ValueError, IndexError):
        return False, date


def date1_conditions(date1):
    date_list = []
    month_written = date1[0]
    day = date1[1].removesuffix(",")
    year = date1[2]
    months_dic = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    # verify month in list and day (1 to 31)
    if (month_written in months_dic) and (1 <= int(day) <= 31):
        month_number_str = months_dic[month_written]
        date_list.append(day)
        date_list.append(month_number_str)
        date_list.append(year)
        # returns a list organized like: [month_str, day_str, year_str]
        return True, date_list
    else:
        return False, date_list


def date2_type(date):
    date = date.split("/")
    try:
        month = date[0]
        day = date[1]
        return True, date
    except IndexError:
        # if entered here, it's bcs the date given is like: "8 September, 2004" - starts with number but is not a date2 type
        return False, []


def date2_conditions(date2):
    date_list = []
    month = date2[0]
    day = date2[1]
    year = date2[2]
    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
        date_list.append(day)
        date_list.append(month)
        date_list.append(year)
        # returns list: [day_str, month_str, year_str]
        return True, date_list
    else:
        return False, date_list


main()