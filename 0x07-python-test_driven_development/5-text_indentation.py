#!/usr/bin/python3
'''Function  that prints a text with 2 new lines after each of these characters: ., ? and :'''


def text_indentation(text):
    '''
    Print a text with 2 new lines after these characters : . ?
    
    Return: print text
    '''
    
    if type(text) is not str:
        raise TypeError('text must be a string')
    
    new = True
    for i in text:
        if not (new and i ==' '):
            print(i, end='')
            new = False
            if i in '.?:':
                print('\n')
                new = True