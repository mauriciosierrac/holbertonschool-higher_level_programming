#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenght = len(my_list)
    if idx < 0 or idx > lenght:
        return (my_list)
    else:
        for i in list(range(lenght)):
            if idx == i:
                my_list[i] = element
    return (my_list)