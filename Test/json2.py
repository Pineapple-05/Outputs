import json

with open("json1.json") as file:
    data = json.load(file)

    for item in data:
        print(f"{item['NAME']} has the birthday {item['DOB']}")
