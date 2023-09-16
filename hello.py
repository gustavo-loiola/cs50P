'''
# ask user for their name
name = input("What's yor name? ")

# remove whitespace from str
name = name.strip()

"""
# Capitalize user's name (nn pode usar antes do strip, pq se tiver espaço nn vai "capitalizar")
name = name.capitalize()
"""

# Capitalize user's name (capitalize todas as primeiras letras)
name = name.title()
'''

'''
# Ask user for their name, remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split()

# Say hello to user
print("Hello,", first)
print(f"Hello, {last}")
'''

def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to):
    print("hello,", to)

main()