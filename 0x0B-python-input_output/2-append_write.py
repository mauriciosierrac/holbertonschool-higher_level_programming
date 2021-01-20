#!/usr/bin/python3
'''append string to end of text file'''


def append_write(filename="", text=""):
    '''this function append a string to end of file.txt'''
    with open(filename, 'a') as file:
        return file.write(text)
