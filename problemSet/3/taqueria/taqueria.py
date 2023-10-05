def main():
    total_cost = 0

    while True:
        item_cost = get_item("Item: ")
        if item_cost != "stop program":
            total_cost += item_cost
            print(f"Total: ${total_cost:.2f}")
        else:
            print()
            break


def get_item(prompt):
    item = ""
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while item not in menu:
        try:
            item = input(prompt).title()
        except EOFError:
            return "stop program"
    return menu[item]


main()