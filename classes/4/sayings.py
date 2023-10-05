def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


#main() is coded like this bcs when I import this archive to use one of it's functions (e.g. hello)
# it doesn't run all the code and executes the main function
# but it does read the main function when I run this program by myself
# the variable __name__ is a special symbol in Python whose value is automatically set by Python
# to be "main" when you run a file from the command line as by running "python sayings.py"
if __name__ == "__main__":
    main()