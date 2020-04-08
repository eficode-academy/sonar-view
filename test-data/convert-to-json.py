import csv
import json
import os
from random import randint

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)                                       

#Only run once to Fetch from CSV to JSON

with open('test-data/test.csv', 'r') as f:
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
        
with open('test-data/test.json', 'w') as f:
    json.dump(json_data, f)

new_json = []
with open('test-data/test.json', 'r') as data:
    json_data = json.load(data)

    for item in json_data:
        repeat_dict = {} 
        team_dict = {}
        survey_dict= {}
        survey_dict["survey"] = []
        repeat_dict["Persons"] = []
        for key in list(item.keys()):
            if key == "For Finland: What team are you in?":
                team_dict["Team"] = item[key]
                repeat_dict["Persons"][0].update(team_dict)
            if key == "Timestamp":
                repeat_dict["Survey Date"] = item["Timestamp"]
                repeat_dict["Persons"].append({
                    "Email":item["Email Address"],
                    "Office":item["What office are you situated in?"],
                    "Name":item["Name"]
                })
            if "How is your proficiency in the following tools/technologies/skills:" in key:
                skills = {}
                new_key = key.replace("How is your proficiency in the following tools/technologies/skills: ", "")
                item[new_key] = item.pop(key)
                
                skills.update({
                    "name":new_key,
                    "level":item[new_key]
                })
                survey_dict["survey"].append(skills)
        repeat_dict["Persons"][0].update(survey_dict)
        new_json.append(repeat_dict)

with open('test-data/test.json', 'w') as f:
    json.dump(new_json, f)


