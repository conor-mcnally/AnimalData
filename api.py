import requests
import json
import pandas as pd
import os
import folium

#Retrive Data
#This is a public API so no need for key/token this time
# url = "http://www.bloowatch.org/developers/json/species"
# data = requests.get(url)
# animals = data.json()
# with open("animals.json", "w") as file:
#     json.dump(animals, file)
#Test Print
# print(json.dumps(animals, indent=4))
#You need to start file after first 3 lines
#I just done this manually

#Put data into dataframe
df = pd.read_json('animals.json')
filtered = df.filter(['name', 'location', 'population', 'status', 'image'])

#Visualise Data
m = folium.Map()
m
