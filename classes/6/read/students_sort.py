students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        '''
        student = {}
        student["name"] = name
        student["house"] = house
        '''
        #pythonic way to do the above
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# notice that the function sorted is using as parameteres
# students, which is a list
# key=get_name to tell sorted that is to sort based what key equals to, in this case is the
# function get_name, that was created to return the value of the key "name" that is inside of
# variable student, which is a dictionary
# by default reverse=False so we can ommit. but if we want reverse, we declare reverse=True
# obs: not calling get_name manually (i.e. not using "get_name()"). The function sorted calls it automatically
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

'''
pythonic way:
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
'''