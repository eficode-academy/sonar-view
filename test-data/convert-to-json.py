import csv
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__)) 
print(current_dir)                                       

with open('test-data/test.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('test-data/test.json', 'w') as f:
    json.dump(rows, f)