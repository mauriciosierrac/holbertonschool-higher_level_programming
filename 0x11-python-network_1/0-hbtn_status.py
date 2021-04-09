#!/usr/bin/python3
import urllib.request

# with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
#     html = response.read()
#     print(html)

response = request.get('http://intranet.hbtn.io/status')
print(response)
