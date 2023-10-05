def main():
    mass = int(input("m: "))
    energy = formula(mass)
    print(f"E: {energy}")


def formula(m):
    c = 3 * (10**8)
    return m * (c**2)


main()
