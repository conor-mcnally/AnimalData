import requests
import json

#Retrive Data
#This is a public API so no need for key/token this time
url = "http://www.bloowatch.org/developers/json/species"
data = requests.get(url)
animals = data.json()
with open("animals.json", "w") as file:
    json.dump(animals, file)
#Test Print
# print(json.dumps(animals, indent=4))
