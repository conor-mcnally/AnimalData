import requests
import json
import pandas as pd

#Retrive Data
#This is a public API so no need for key/token this time
url = "http://www.bloowatch.org/developers/json/species"
data = requests.get(url)
json_data = data.json()
with open("animals.json", "w") as file:
    json.dump(json_data, file)

#Process data
with open("animals.json", "r") as file:
    animal_data = json.load(file)

#Animal data = all data


#Visualise Data
