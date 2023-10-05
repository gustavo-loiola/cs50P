def main():
    n = int(input("Square size: "))
    print_square(n)

def print_square(size):
    for i in range(size):
        print("#" * size)
        
main()