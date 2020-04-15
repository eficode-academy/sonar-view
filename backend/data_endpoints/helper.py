import json
import os
from google.cloud import firestore


def fetch_all_date():
    db = firestore.Client()
    surveys = db.collections()
    surveys_date = {}
    for index, survey in enumerate(surveys):
        surveys_date[index]=survey.id
    return surveys_date

def fetch_each_survey_person(id):
    db = firestore.Client()
    doc_ref = db.collection(id)
    survey_names = doc_ref.stream()
    each_survey_person = {}
    for index, doc in enumerate(survey_names):
        each_survey_person[index] = doc.id
    each_name = fetch_each_name(id, each_survey_person)
    return each_name

def fetch_each_name(id, each_survey_person):
    db = firestore.Client()
    doc_ref = db.collection(id)
    for key in each_survey_person:
        all_items = doc_ref.document(each_survey_person[key]).collection("Person").get()
    return all_items
