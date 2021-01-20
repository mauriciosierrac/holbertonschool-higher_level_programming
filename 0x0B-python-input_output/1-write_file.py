#!/usr/bin/python3
'''write in external file'''


def write_file(filename="", text=""):
    '''that method write in external file'''
    with open(filename, 'w') as file:
        return file.write(text)
