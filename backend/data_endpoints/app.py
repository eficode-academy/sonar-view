import shutil
import json
import os
from flask import Flask, request, Blueprint
from flask_cors import CORS, cross_origin
from datetime import date
from os import path
from config import CSV_TMP_PATH
from google.cloud import firestore
from helper import fetch_all_date, fetch_each_survey_person, fetch_person_detail, get_names, get_surveys, get_survey_items, csv_to_json, construct_response, is_correct_name

survey = Blueprint('home', __name__, template_folder='templates', static_folder='static')
@cross_origin()

# Post a survey
@survey.route('/surveys', methods=['POST'])
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
        if item["person"][0]["email"]:
            # Employee Email as document name
            document_name = item["person"][0]["email"]
            name_list.append(document_name)
            # In the db design, we put all answers in a survey as a collection, 
            # each person's answer and a document 
            db.collection(survey_collection).document(document_name).set(item) 
    return construct_response('Successfully wrote to storage', survey_collection, name_list)

@survey.route('/surveys', methods=['GET'])
def surveys_names():
    try:
        surveys_date = fetch_all_date()
        return surveys_date, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@survey.route('/surveys/<id>/persons', methods=['GET'])
def persons_names(id):
    try:
        each_survey_person_name = fetch_each_survey_person(id)
        return each_survey_person_name, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@survey.route('/surveys/<id>/persons/<name_id>', methods=['GET'])
def person_detail(id, name_id):
    try:
        person_detail = fetch_person_detail(id, name_id) 
        return (person_detail)
    except Exception as e:
        return f"An Error Occured: {e}"

@survey.route('/persons', methods=['GET'])
def all_person_name():
    try:
        get_name = get_names()
        return get_name, 200
    except Exception as e:
        return f"An Error Occured: {e}"


@survey.route('/persons/<id>/surveys', methods=['GET'])
def all_survey_for_person(id):
    try:
        get_survey = get_surveys(id)
        return get_survey, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@survey.route('/persons/<id>/surveys/<survey_id>', methods=['GET'])
def all_survey_item(id, survey_id):
    try:
        get_survey_item = get_survey_items(id, survey_id)
        return get_survey_item, 200
    except Exception as e:
        return f"An Error Occured: {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app = Flask(__name__)
    cors = CORS(app)
    app.register_blueprint(survey, url_prefix='/sonar')
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)