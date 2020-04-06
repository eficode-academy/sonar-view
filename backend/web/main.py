from flask import escape, Flask
from data_helper import format_to_json
from google.cloud import firestore
import google.cloud.exceptions

def sonar_survey(request):
    db = firestore.Client()
    request_csv = request.files['data']
    if not request_csv:
        return 'Upload a CSV file'
    print(request_csv)
    json_data = format_to_json(request_csv)
    print(json_data)
    db.collection('sonar').document('TkXdYUqqliiKrMVNO07J').set(json_data) #firestore name, must be in same project namespace
    db.collection('sonar').document('foo').set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })
    return "OK"
