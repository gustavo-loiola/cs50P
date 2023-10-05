def main():
    n = int(input("Square size: "))
    print_square(n)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")

        print()

main()