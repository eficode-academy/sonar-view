import csv
import json
import os
from random import randint

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)     

with open('test-data/surveypal-data-in.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('test-data/test1.json', 'w') as f:
    json.dump(rows, f)

with open('test-data/test1.json', 'r') as data:
    json_data = json.load(data) 
    for item in json_data:
        if item['Name']:
            item['Name'] = "Sara Parker-"+str(randint(100, 999))
            item['Email'] = item['Name']+"@eficode.com"
    for item in json_data:
        for key in list(item.keys()):
            if (item[key]==''or item[key]=="Don't know it" or key=="Language" or key=="Finished" or key=="Answer ID" or key=="Duration (in minutes)" or key=="Survey ID"):
                del item[key]
with open('test-data/test1.json', 'w') as f:
    json.dump(json_data, f)

new_json = []
with open('test-data/test1.json', 'r') as data:
    json_data = json.load(data)
    for item in json_data:
        repeat_dict = {} 
        team_dict = {}
        survey_dict= {}
        survey_dict["survey"] = []
        repeat_dict["Persons"] = []
        for key in list(item.keys()):
            if key == "Started":
                repeat_dict["Survey Date"] = item["Started"]
                repeat_dict["Persons"].append({
                    "Email":item["Email"],
                    "Office":item["Where you come from"],
                    "Name":item["Name"]
                })
            if (key != "Started" and key != "Email" and key != "Where you come from" and key != "Name" ):
                skills = {}
                skills.update({
                    "name":key,
                    "level":item[key]
                })
                survey_dict["survey"].append(skills)
        repeat_dict["Persons"][0].update(survey_dict)
        new_json.append(repeat_dict)

with open('test-data/test1.json', 'w') as f:
    json.dump(new_json, f)

