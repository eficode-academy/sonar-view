import os
import json
from datetime import date
import shutil
from os import path
from flask import escape, Flask
from helper import csv_to_json
from config import CSV_TMP_PATH
from google.cloud import firestore
import google.cloud.exceptions

def sonar_survey(request):
    db = firestore.Client()
    csv_file_path = CSV_TMP_PATH
    request_csv = request.files['data']
    if not request_csv:
        return 'No file in the POST request'
    request_csv.save(csv_file_path)
    json_data = csv_to_json(csv_file_path)
    today = date.today()
    survey_period = str(today.month)+'/'+str(today.year)
    for item in json_data:
            if item["Person"][0]["Name"]:
                document_name = item["Person"][0]["Name"]
                #replace survey below with survey_peroid
                db.collection("survey").document(document_name).set(item) 
    return 'Successfully wrote to storage'
