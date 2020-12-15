#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        lenght = len(my_list)
        my_list.reverse()
        for i in list(range(lenght)):
                print("{}".format(my_list[i]))
