import csv
import json
import os
from random import randint
from datetime import date

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)                                       

#Only run once to Fetch from CSV to JSON

with open('test-data/data.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('test-data/test.json', 'w') as f:
    json.dump(rows, f)

with open('test-data/test.json', 'r') as data:
    json_data = json.load(data) 
    for item in json_data:
        if item['Name']:
            item['Name'] = "Sara Parker-"+str(randint(100, 999))
            item['Email Address'] = item['Name']+"@eficode.com"
    for item in json_data:
        for key in list(item.keys()):
            if (item[key]=='' or item[key]=="Don't know it"):
                del item[key]
    new_json = []
    for item in json_data:
        repeat_dict = {} 
        team_dict = {}
        survey_dict= {}
        survey_dict["survey"] = []
        repeat_dict["Person"] = []
        today=date.today()
        survey_period=str(today.month)+'/'+str(today.year)
        for key in list(item.keys()):
            if key == "Team":
                team_dict["Team"] = item[key]
                repeat_dict["Person"][0].update(team_dict)
            if key == "Name":
                repeat_dict["Person"].append({
                    "Email":item["Email"],
                    "Office":item["Office"],
                    "Name":item["Name"],
                })
            if (key != "Team" and key != "Email" and key != "Office" and key != "Name" ):
                skills = {}
                skills.update({
                    "name":key,
                    "level":item[key]
                })
                survey_dict["survey"].append(skills)
        repeat_dict["Person"][0].update(survey_dict)
        new_json.append(repeat_dict)

with open('test-data/test.json', 'w') as f:
    json.dump(new_json, f)
