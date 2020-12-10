#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    n = len(argv)

    if n == 4:
        a = int(argv[1])
        b = int(argv[3])
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    elif argv[2] != '+' or argv[2] != '-' or argv[2] != '*' or argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
