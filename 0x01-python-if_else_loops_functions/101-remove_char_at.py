#!/usr/bin/python3
def remove_char_at(str, n):
    p = 0
    str2 = ""
    for i in (str):
        if p != n:
            str2 = str2 + i
        p = p + 1
    return(str2)
