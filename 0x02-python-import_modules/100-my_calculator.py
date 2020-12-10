#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)

    if n == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
    elif argv[2] != '+' or argv[2] != '-' or argv[2] != '*' or argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
