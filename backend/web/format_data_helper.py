import csv
import json
import os
from random import randint

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)                                       

def format_to_json():
    try:
        with open('test-data/large-test.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open('test-data/large-test.json', 'w') as f:
            json.dump(rows, f)

        with open('test-data/large-test.json', 'r') as data:
            for item in json_data:
                for key in list(item.keys()):
                    if "How is your proficiency in the following tools/technologies/skills:" in key:
                        new_key = key.replace("How is your proficiency in the following tools/technologies/skills: ", "")
                        item[new_key] = item.pop(key)

        with open('test-data/large-test.json', 'w') as f:
            json.dump(json_data, f)
    except Exception as e:
        print("Unfortunately CSV cannot be changed to JSON format" + str(e))













#Only run for mock data

# with open('test-data/large-test.json', 'r') as data:
#     json_data = json.load(data) 
#     for item in json_data:
#         if item['Name']:
#             item['Name'] = "Sara Parker-"+str(randint(100, 999))
#             item['Email Address'] = item['Name']+"@eficode.com"
#     for item in json_data:
#         for key in list(item.keys()):
#             if (item[key]=='' or item[key]=="Don't know it"):
#                 del item[key]
        
# with open('test-data/large-test.json', 'w') as f:
#     json.dump(json_data, f)


