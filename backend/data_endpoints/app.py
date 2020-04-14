import os
import shutil
import json

from flask import Flask, request
from datetime import date
from os import path
from helper import csv_to_json, construct_response, is_correct_name
from config import CSV_TMP_PATH
from google.cloud import firestore

app = Flask(__name__)

# Post a survey
@app.route('/surveys', methods=['POST'])
def add_sonar_survey():
    name_list = []
    db = firestore.Client()
    csv_file_path = CSV_TMP_PATH
    request_csv = request.files['data']
    survey_collection = request.form.get('name')
    if not survey_collection or not is_correct_name(survey_collection):
        return construct_response('Collection name should be named by survey date (YYYY-MM)', date.today().strftime("%Y-%m"), name_list), 400
    if not request_csv:
        return construct_response('No file in the POST request', survey_collection, name_list), 400
    if request_csv.filename.split('.')[-1].lower() != 'csv':
        return construct_response('File extension error, *.csv file required',  survey_collection, name_list), 400
    request_csv.save(csv_file_path)
    json_data = csv_to_json(csv_file_path)
    # The collection name is YYYY-MM
    for item in json_data:
        if item["Person"][0]["Email"]:
            # Employee Email as document name
            document_name = item["Person"][0]["Email"]
            name_list.append(document_name)
            # In the db design, we put all answers in a survey as a collection, 
            # each person's answer and a document 
            db.collection(survey_collection).document(document_name).set(item) 
    return construct_response('Successfully wrote to storage', survey_collection, name_list)

@app.route('/surveys', methods=['GET'])
def surveys_names():
    db = firestore.Client()
    cols = db.collections()
    list_col = []
    for col in cols:
        list_col.append(col.id)
    result = list_col[0]
    return result

port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)