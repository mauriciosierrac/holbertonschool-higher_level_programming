#!/usr/bin/python3

import requests
from sys import argv


data = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
print(data.json().get('id'))
