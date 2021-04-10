#!/usr/bin/python3
'''method get API github'''


import requests
from sys import argv

if __name__ == '__main__':
    
    data = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(data.json().get('id'))
