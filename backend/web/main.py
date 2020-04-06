import os
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
    # The json format of test data currently incorrect, Firstore doesn't accept an array as the document content.
    # So temporary take the first element as the document content.
    db.collection('sonar').document('foo').set(json_data[0]) 
    return json_data[0]
