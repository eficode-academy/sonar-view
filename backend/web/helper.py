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
            for key in item.keys():
                if "How is your proficiency in the following tools/technologies/skills:" in key:
                    new_key = key.replace("How is your proficiency in the following tools/technologies/skills: ", "")
                    item[new_key] = item.pop(key)
    os.remove(json_tmp_path)
    os.remove(file_path)
    return json_data
