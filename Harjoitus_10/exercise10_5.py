import os
import json

os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
fileName = "countries.json"

if os.path.exists(fileName):
        try:
            with open(fileName, "r") as file:
                countries = json.load(file)
        except json.JSONDecodeError:
            fileData = {}
else:
    fileData = {}

for i in range(len(countries)):
    print(f"{countries[i]['country']}: {countries[i]['capital']}")