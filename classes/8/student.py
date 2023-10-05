class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus == "Stag":
            return "Stag Emoji"
        elif self.patronus == "Otter":
            return "Otter emoji"
        else:
            return "Magic wand emoji"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

main()