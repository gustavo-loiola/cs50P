def main():
    time = input("What times is it? ")
    sufix, time = Fsufix(time)

    if sufix == True:
        time = convert(time) + 12
    else:
        time = time.removesuffix(" a.m.")
        time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print()

def convert(time):
    hours, minutes = str(time).split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)

def Fsufix(time):
    time, space, sufix = time.rpartition(" ")

    if sufix == "p.m.":
        return True, time
    elif sufix == "a.m.":
        return False, time
    else:
        return False, sufix

if __name__== "__main__":
    main()