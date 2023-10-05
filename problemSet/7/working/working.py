import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(\d+(:\d+)?) (AM|PM) to (\d+(:\d+)?) (AM|PM)$", s, re.ASCII
    ):
        time1 = matches.group(1).split(":")
        time2 = matches.group(4).split(":")

        if len(time1) == 1:
            time1.append("0")
        if len(time2) == 1:
            time2.append("0")

        time1.append(matches.group(3))
        time2.append(matches.group(6))

        if verify_time(time1) and verify_time(time2):
            times = [time1, time2]
            for time in times:
                make_int(time)
                if time[0] == 12:
                    if time[2] == "AM":
                        time[0] = 0
                elif time[2] == "PM":
                    time[0] = time[0] + 12
            return f"{time1[0]:02}:{time1[1]:02} to {time2[0]:02}:{time2[1]:02}"
        else:
            raise ValueError
    else:
        raise ValueError


def verify_time(time_list):
    if 0 <= int(time_list[0]) <= 12 and 0 <= int(time_list[1]) <= 59:
        return True
    else:
        return False


def make_int(time_l):
    time_l[0] = int(time_l[0])
    time_l[1] = int(time_l[1])
    return time_l


if __name__ == "__main__":
    main()
