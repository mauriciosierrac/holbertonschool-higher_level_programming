#!/usr/bin/python3
'''comment'''
import json
import sys


def save_to_json_file(my_obj, filename):
    '''write in json object'''
    with open(filename, 'w') as outfile:
        return json.dump(my_obj, outfile)
