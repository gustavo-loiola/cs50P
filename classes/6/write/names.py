# input for the name
name = input("What's your name? ")

# creates a txt file called names and 'w'rites on it
with open("names.txt", "w") as file:
    file.write(f"{name}\n")