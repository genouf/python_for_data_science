import sys

if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

if len(sys.argv) == 1:
    raise AssertionError("no argument is provided")

first_arg = sys.argv[1]

try:
    number = int(first_arg)
    if (number % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    raise AssertionError("argument is not an integer")