import requests
import json

response=requests.get('http://wethinkcode.co.za')
print(response)

#remember we are using flask
#we are also using Rest api 

"""Make a api that gets all university names and all the courses they offer and use this api in live demo session of the actual app that you are building"""