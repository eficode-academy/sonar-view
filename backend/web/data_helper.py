import csv
import json
import os
from random import randint
                                      

def format_to_json(request_csv):
    try:
        file_path = '/tmp/sonar.csv'
        content = request_csv

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open('file_path', 'wb') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open('/tmp/sonar.json', 'w') as f:
            json.dump(rows, f)

        with open('/tmp/sonar.json', 'r') as data:
            json_data = json.load(data)
            for item in json_data:
                for key in list(item.keys()):
                    if "How is your proficiency in the following tools/technologies/skills:" in key:
                        new_key = key.replace("How is your proficiency in the following tools/technologies/skills: ", "")
                        item[new_key] = item.pop(key)

        with open('/tmp/sonar.json', 'w') as f:
            json.dump(json_data, f)
        return json_data
    except Exception as e:
        print("Unfortunately CSV cannot be changed to JSON format" + str(e))


# def store_to_firestore(request, json_data):
#     try:
#         doc_ref = db.collection('sonar').document('5okuD96EdJ2Pflmx1dKZ')
#         doc = doc_ref.get()
#         if doc.exists:
#             return jsonify(doc.to_dict())
#         else:
#             doc_ref.set({'name': 'Hello'})
#             return 'UPDATED'



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


