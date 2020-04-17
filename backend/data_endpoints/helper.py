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
    survey_date['surveys'] = [] 
    for index, survey in enumerate(survey_collection):
        survey_date['surveys'].append({
            index:survey.id
        }) 
    return survey_date
  

def fetch_each_survey_person(id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    survey_names = doc_ref.stream()
    each_survey_person = {}
    each_name = {}
    each_name["persons"] = []
    for index, doc in enumerate(survey_names):
        each_survey_person[index] = doc.id
    for (k, email) in each_survey_person.items():
        each_name["persons"].append({
            "email":email,
            "name":doc_ref.document(email).get().to_dict()['person'][0]['name']
            })
    return each_name

def fetch_person_detail(id, name_id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    person_detail = {name_id: doc_ref.document(name_id).get().to_dict()['person'][0]}
    return person_detail
    
def get_names():
    db = firestore.Client()
    collections_name = fetch_all_date()
    each_name = {}
    all_names = {}
    all_names["persons"] = []
    each_name["persons"] = []
    for item in collections_name['surveys']:
        coll_list = item.values()
        coll_name = ''.join(coll_list)
        doc_ref = db.collection(coll_name)
        doc_name = doc_ref.stream()
        for item in doc_name:
            name_item = doc_ref.document(item.id).get().to_dict()['person'][0]['name']
            each_name["persons"].append({
                "email":item.id,
                "name":name_item
            })
    all_names["persons"] = list({v['email']:v for v in each_name["persons"]}.values())
    return all_names


def get_surveys(id):
    db = firestore.Client()
    collections_name = fetch_all_date()
    all_name = {}
    all_name["surveys"] = []
    for item in collections_name['surveys']:
        coll_list = item.values()
        coll_name = ''.join(coll_list)
        doc_ref = db.collection(coll_name)
        doc_name = doc_ref.stream()
        for index, doc in enumerate(doc_name):
            if(doc.id == id):
                all_name["surveys"].append({
                    index:coll_name
                })
    final_name = {id: all_name}
    return final_name


def get_survey_items(person_id, survey_id):
    db = firestore.Client()
    doc_ref = db.collection(survey_id).document(person_id)
    survey_items = {}
    survey_items["survey"] = []
    survey_items["email"] = person_id
    survey_item = doc_ref.get().to_dict()['person'][0]['survey']
    survey_items["survey"].append(survey_item)
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
        for key in list(item.keys()):
            if (item[key]==''):
                del item[key]      
    new_json = []
    for item in json_data:
        repeat_dict = {}
        team_dict = {}
        survey_dict = {}
        survey_dict["survey"] = []
        repeat_dict["person"] = []
        for key in list(item.keys()):
            if key == "Team":
                team_dict["team"] = item[key]
                repeat_dict["person"][0].update(team_dict)
            if key == "Name":
                repeat_dict["person"].append({
                    "email":item["Email"],
                    "office":item["Office"],
                    "name":item["Name"],
                })
            if (key != "Team" and key != "Email" and key !=
                    "Office" and key != "Name"):
                skills = {}
                skills.update({
                    "name": key,
                    "level": item[key]
                })
                survey_dict["survey"].append(skills)
        repeat_dict["person"][0].update(survey_dict)
        new_json.append(repeat_dict)
    os.remove(json_tmp_path)
    os.remove(file_path)
    return new_json


def construct_response(
        msg: str,
        collection: str,
        name: list,
        user: str = None):
    return {
        'msg': msg,
        'collection': collection,
        'persons': name,
        'current_user': user}


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
