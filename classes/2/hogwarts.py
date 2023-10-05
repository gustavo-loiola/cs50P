#using dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

#instead of using numbers as the index, as we used in lists, now we use strings. Ex: print(students["Hermione"])

for student in students:
    print(student, students[student], sep=", ")
