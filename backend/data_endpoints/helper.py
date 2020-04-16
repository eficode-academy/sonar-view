import json
import os
import jwt
from google.cloud import firestore, logging
import csv
import re
from datetime import datetime
from random import randint
from config import SECRET_KEY
from flask import jsonify, request
from functools import wraps


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
    each_name["Persons"] = []
    for item in collections_name:
        doc_ref = db.collection(collections_name[item])
        doc_name = doc_ref.stream()
        for item in doc_name:
            name_item = doc_ref.document(item.id).get().to_dict()['Person'][0]['Name']
            if name_item not in each_name.values():
                each_name["Persons"].append({
                "email":item.id,
                "name":name_item
                })
    return each_name

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

def construct_response(msg: str, collection: str, name: list, user: str = None):
    return {'msg': msg, 'collection':collection, 'persons': name, 'current_user': user}

def is_jwt_valid(headers):
    if not headers.get('Authorization'):
        return [False, "No authorization header"]
    try:
        scheme, token = headers['Authorization'].strip().split(' ', 1)
        if scheme.lower() != 'bearer':
            raise ValueError()
    except ValueError:
        return [False, "Invalid authorization header"]
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return [True, decoded]
    except jwt.InvalidTokenError as exc:
        return [False, str(exc)]

def generate_jwt_token(**kwargs):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = kwargs
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = is_jwt_valid(request.headers)
        if not res[0]:
            return jsonify(msg='Login required!'), 403
        else:
            return fn(res[1], *args, **kwargs)
    return wrapper