#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if idx < 0 or idx > lenght:
        return (None)
    else:
        for i in list(range(lenght)):
            if i == idx:
                return (my_list[i])
