# this is going to be a script for learning api calls

# this is always the section for importing modules

import requests

# http://api.open-notify.org/astros.json
# Logic
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
number = str(json['number'])
people = str(json['people'])

# Executables
print(number + people)