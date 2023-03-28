import json

file_path = "capital_cities.json"
with open(file_path) as file:
    data = json.load(file)
    for record in data["countries"]:
        country = record["country"]
        capital = record["capital"]
        print(f"Capital of {country} is {capital}")