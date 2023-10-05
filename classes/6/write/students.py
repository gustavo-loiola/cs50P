import csv

name = input("what's your name? ")
home = input("what's your home? ")


with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])