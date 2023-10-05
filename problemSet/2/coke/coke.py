def main():
    amount_due = 50

    while amount_due > 0:
        coin = get_coin()
        amount_due = amount_due - coin
        if amount_due == 0:
            print("Change Owed: 0")
        elif amount_due < 0:
            change = - amount_due
            print("Change Owed:", change)
        else:
            print("Amount Due:", amount_due)

def get_coin():
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        return 0

main()