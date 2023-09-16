'''
x = float(input("What's x? "))
y = float(input("What's y? "))

# z = round (x / y, 3)
# print(z)

z = x / y
print(f"{z:.3f}")
'''

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2


if __name__ == '__main__':
    main()