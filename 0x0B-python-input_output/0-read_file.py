#!/usr/bin/python3
'''read the external file'''


def read_file(filename=""):
    '''that method call external file, read and print the file'''
    with open(filename) as file:
        print(file.read(), end="")
