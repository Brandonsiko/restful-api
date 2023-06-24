import requests
import json

#THIS IS HOW WE CONSUME AN API
response=requests.get('http://wethinkcode.co.za')
data=response.json()['items']

for item in data:
    print(item)

#THIS IS HOW WE MAKE AN API

