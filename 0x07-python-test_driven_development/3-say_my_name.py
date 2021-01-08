#!/usr/bin/python3
''' That Function print the first and last name'''


def say_my_name(first_name, last_name=""):
    '''
    funcion say my name
    
    Return: print the first and last name
    '''
    
    
    if type(first_name) is not str:
        raise TypeError ('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError ('last_name must be a string')
    
    print('My name is {} {}'.format(first_name, last_name))