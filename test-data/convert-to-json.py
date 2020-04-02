import csv
import json
import os
from random import randint

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)                                       

with open('test-data/large-test.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('test-data/large-test.json', 'w') as f:
    json.dump(rows, f)

with open('test-data/large-test.json', 'r') as data:
    json_data = json.load(data) 
    for item in json_data:
        if item['Name']:
            item['Name'] = "Sara Parker-"+str(randint(100, 999))
            item['Email Address'] = item['Name']+"@eficode.com"

with open('test-data/large-test.json', 'w') as f:
    json.dump(json_data, f)
