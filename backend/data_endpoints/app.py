import os
from flask import Flask, request, jsonify, Blueprint, json
from google.cloud import firestore
from helper import fetch_all_date, fetch_each_survey_person

survey = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@survey.route('/surveys', methods=['GET'])
def surveys_names():
    surveys_date = fetch_all_date()
    return surveys_date

@survey.route('/surveys/<id>/persons', methods=['GET'])
def persons_names(id):
    each_survey_person_name = fetch_each_survey_person(id)
    return each_survey_person_name



port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(survey, url_prefix='/sonar')
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)