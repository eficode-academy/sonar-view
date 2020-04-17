import json
import os
from google.cloud import firestore, logging
import csv
import re
from datetime import datetime
from random import randint


client = logging.Client()     
logger = client.logger('endpoints-logger') 


def fetch_all_date():
    db = firestore.Client()
    survey_collection = db.collections()
    survey_date = {}
    for index, survey in enumerate(survey_collection):
        survey_date[index] = survey.id
    return survey_date

def fetch_each_survey_person(id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    survey_names = doc_ref.stream()
    each_survey_person = {}
    each_name = {}
    each_name["Persons"] = []
    for index, doc in enumerate(survey_names):
        each_survey_person[index] = doc.id
    for (k, email) in each_survey_person.items():
        each_name["Persons"].append({
            "email":email,
            "name":doc_ref.document(email).get().to_dict()['Person'][0]['Name']
            })
    return each_name

def fetch_person_detail(id, name_id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    person_detail = {name_id: doc_ref.document(name_id).get().to_dict()['Person'][0]}
    return person_detail
    
def get_names():
    db = firestore.Client()
    collections_name = fetch_all_date()
    each_survey_doc = {}
    each_name = {}
    all_names = {}
    all_names["Persons"] = []
    each_name["Persons"] = []
    for item in collections_name:
        doc_ref = db.collection(collections_name[item])
        doc_name = doc_ref.stream()
        for item in doc_name:
            name_item = doc_ref.document(item.id).get().to_dict()['Person'][0]['Name']
            each_name["Persons"].append({
                "email":item.id,
                "name":name_item
            })
    all_names["Persons"] = list({v['email']:v for v in each_name["Persons"]}.values())
    return all_names

def get_surveys(id):
    db = firestore.Client()
    collections_name = fetch_all_date()
    all_name = {}
    all_name["Surveys"] = []
    for item in collections_name:
        doc_ref = db.collection(collections_name[item])
        doc_name = doc_ref.stream()
        for index, doc in enumerate(doc_name):
            if(doc.id == id):
                all_name["Surveys"].append({
                    index:collections_name[item]
                })
    final_name = {id: all_name}
    return final_name

def get_survey_items(person_id, survey_id):
    db = firestore.Client()
    doc_ref = db.collection(survey_id).document(person_id)
    survey_items = {}
    survey_items["Survey"] = []
    survey_items["email"] = person_id
    survey_item = doc_ref.get().to_dict()['Person'][0]['survey']
    survey_items["Survey"].append(survey_item)
    return survey_items

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
        # if item['Name']:
        #     item['Name'] = "Sara Parker-"+str(randint(100, 999))
        #     item['Email'] = item['Name']+"@eficode.com"
        for key in list(item.keys()):
            if (item[key]==''):
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
