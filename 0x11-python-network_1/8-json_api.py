#!/usr/bin/python3
'''the script tha takes in a letter ans send a post request to a url'''


import requests
from sys import argv


if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    req = requests.post(url, data=data)
    try:
        json_answ = req.json()
        if json_answ:
            print("[{}] {}".format(json_answ['id'], json_answ['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
