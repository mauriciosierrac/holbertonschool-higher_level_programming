#!/usr/bin/python3
'''comment'''
import json


def load_from_json_file(filename):
    '''create object from a json file
    PARAMETERS:
    filename: json file name
    '''
    with open(filename) as f:
        return json.load(f)
