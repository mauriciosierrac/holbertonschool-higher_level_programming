#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)
    new_list = my_list.copy()
    if idx < 0 or idx > lenght:
        return (new_list)
    else:
        for i in list(range(lenght)):
            if idx == i:
                new_list[i] = element
    return (new_list)
