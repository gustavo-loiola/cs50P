with open("students.csv") as file:
    for line in file:
        # pythonic way:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

        '''
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        '''