#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resul = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                resul.append(0)
            else:
                resul.append(1)
        return (resul)
