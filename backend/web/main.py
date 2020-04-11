import os
import json
from datetime import date
import shutil
from os import path
from flask import escape, Flask
from helper import csv_to_json, construct_response
from config import CSV_TMP_PATH
from google.cloud import firestore
import google.cloud.exceptions

def sonar_survey(request):
    name_list = []
    survey_date = date.today().strftime("%m%Y")
    db = firestore.Client()
    csv_file_path = CSV_TMP_PATH
    request_csv = request.files['data']
    if not request_csv:
        return construct_response('No file in the POST request', survey_date, name_list), 400
    if request_csv.filename.split('.')[-1].lower() != 'csv':
        return construct_response('File extension error, *.csv file required',  survey_date, name_list), 400
    request_csv.save(csv_file_path)
    json_data = csv_to_json(csv_file_path)
    # The collection name is MM/YYYY
    for item in json_data:
        if item["Person"][0]["Name"]:
            # Employee name as document name
            document_name = item["Person"][0]["Name"]
            name_list.append(document_name)
            # In the db design, we use the date that we wrote to the db as the survey date, we
            # put all answers in a survey as a collection, each person's answer and a document 
            db.collection(survey_date).document(document_name).set(item) 
    return construct_response('Successfully wrote to storage', survey_date, name_list)
