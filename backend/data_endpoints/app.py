import shutil
import json
import os

from flask import Flask, request, Blueprint, make_response, jsonify
from flask_cors import CORS, cross_origin
from datetime import date
from os import path
from config import CSV_TMP_PATH, GSUITE_DOMAIN_NAME, CLIENT_ID
from google.cloud import firestore
from helper import *
from google.oauth2 import id_token
from google.auth.transport import requests

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


google_auth = Blueprint('google_login', __name__)
@cross_origin()


# Google auth
@google_auth.route('/auth', methods=['POST'])
@cross_origin()
def authentication():
    token = request.headers.get("Authorization").split(' ')[1]
    
    try:
        if not token:
            raise ValueError('No token')
        
        # Specify the CLIENT_ID of the app that accesses the backend:
        id_info = id_token.verify_oauth2_token(
            token, requests.Request(), CLIENT_ID)
        if id_info['iss'] not in [
            'accounts.google.com',
                'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        # If auth request is from a G Suite domain (eficode.com or eficode.fi):
        if id_info['hd'] not in GSUITE_DOMAIN_NAME:
            raise ValueError('Wrong hosted domain.')
        # ID token is valid. Get the user's Google Account ID from the decoded
        # token.
        jwt_token = generate_jwt_token(
            sub=id_info['sub'],
            exp=id_info['exp'],
            iat=id_info['iat'],
            name=id_info['name'],
            email=id_info['email'])
        return jsonify(msg='Login succeed', auth_token=jwt_token.decode())
    except ValueError as e:
        # Invalid Google token
        return make_response(jsonify(msg='Login failed: {}'.format(e)), 401)
    except KeyError as e:
        return make_response(jsonify(msg='Login failed: {}'.format(e)), 401)

# Post a survey
@google_auth.route('/surveys', methods=['POST'])
# Here's a example When turn on JWT authentication, replace def add_sonar_survey with the code below:
# def add_sonar_survey(payload):
#     user_info = payload
@jwt_required
@cross_origin()
def add_sonar_survey():
    name_list = []
    db = firestore.Client()
    csv_file_path = CSV_TMP_PATH
    request_csv = request.files['data']
    survey_collection = request.form.get('name')
    if not survey_collection or not is_correct_name(survey_collection):
        return construct_response(
            'Collection name should be named by survey date (YYYY-MM)', date.today().strftime("%Y-%m"), name_list), 400
    if not request_csv:
        return construct_response(
            'No file in the POST request', survey_collection, name_list), 400
    if request_csv.filename.split('.')[-1].lower() != 'csv':
        return construct_response(
            'File extension error, *.csv file required', survey_collection, name_list), 400
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
    return construct_response(
        'Successfully wrote to storage',
        survey_collection,
        name_list)
        # No current user info will be returned without adding JWT auth, add below back when add JWT auth
        # ,payload['name'])


@google_auth.route('/surveys', methods=['GET'])
@jwt_required
@cross_origin()
def surveys_names():
    try:
        surveys_date = fetch_all_date()
        return surveys_date, 200
    except Exception as e:
        return f"An Error Occured: {e}"


@google_auth.route('/surveys/<id>/persons', methods=['GET'])
@jwt_required
@cross_origin()
def persons_names(id):
    try:
        each_survey_person_name = fetch_each_survey_person(id)
        return each_survey_person_name, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@google_auth.route('/surveys/<id>/persons/<name_id>', methods=['GET'])
@jwt_required
@cross_origin()
def person_detail(id, name_id):
    try:
        person_detail = fetch_person_detail(id, name_id) 
        return (person_detail)
    except Exception as e:
        return f"An Error Occured: {e}"

@google_auth.route('/persons', methods=['GET'])
@jwt_required
@cross_origin()
def all_person_name():
    try:
        get_name = get_names()
        return get_name, 200
    except Exception as e:
        return f"An Error Occured: {e}"


@google_auth.route('/persons/<id>/surveys', methods=['GET'])
@jwt_required
@cross_origin()
def all_survey_for_person(id):
    try:
        get_survey = get_surveys(id)
        return get_survey, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@google_auth.route('/persons/<id>/surveys/<survey_id>', methods=['GET'])
@jwt_required
@cross_origin()
def all_survey_item(id, survey_id):
    try:
        get_survey_item = get_survey_items(id, survey_id)
        return get_survey_item, 200
    except Exception as e:
        return f"An Error Occured: {e}"


@google_auth.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    print(response)
    return response

port = int(os.environ.get('PORT', 8080))

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'foobar'
app.config['JWT_IDENTITY_CLAIM'] = 'sub'
jwt = JWTManager(app)
jwt.init_app(app)
# app.register_blueprint(survey, url_prefix='/sonar')
app.register_blueprint(google_auth, url_prefix='/google')

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
