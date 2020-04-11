import csv
import json
import os
from random import randint

                                      

def csv_to_json(file_path):
    json_tmp_path = os.path.join(os.path.dirname(file_path), 'sonar.json')
    with open(file_path, newline='') as f:
        try:
            reader = csv.DictReader(f)
        except Exception as e:
            print(e)
        rows = list(reader)
    with open(json_tmp_path, 'w') as f:
        json.dump(rows, f)
    with open(json_tmp_path, 'r') as data:
        json_data = json.load(data) 
    for item in json_data:
        if item['Name']:
            item['Name'] = "Sara Parker-"+str(randint(100, 999))
            item['Email'] = item['Name']+"@eficode.com"
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
    os.remove(json_tmp_path)
    os.remove(file_path)
    return new_json

def construct_response(msg: str, date: str, name: list):
    return {'msg': msg, 'survey-date':date, 'names': name}
