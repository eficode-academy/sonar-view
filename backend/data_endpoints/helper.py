import json
import os
from google.cloud import firestore
import csv
import re
from datetime import datetime
from random import randint

def fetch_all_date():
    db = firestore.Client()
    surveys = db.collections()
    surveys_date = {}
    for index, survey in enumerate(surveys):
        surveys_date[index]=survey.id
    return surveys_date

def fetch_each_survey_person(id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    survey_names = doc_ref.stream()
    each_survey_person = {}
    for index, doc in enumerate(survey_names):
        each_survey_person[index] = doc.id
    each_name = fetch_each_name(id, each_survey_person)
    return each_name

def fetch_each_name(id, each_survey_person):
    db = firestore.Client()
    doc_ref = db.collection(id)
    for key in each_survey_person:
        all_items = doc_ref.document(each_survey_person[key]).collection("Person").get()
    return all_items



def is_correct_name(name):
    try:
        datetime.strptime(name, '%Y-%m')
        return True
    except ValueError:
        return False

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

def construct_response(msg: str, collection: str, name: list):
    return {'msg': msg, 'collection':collection, 'persons': name}
