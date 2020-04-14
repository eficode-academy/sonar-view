import os
from flask import Flask, request, jsonify
from google.cloud import firestore

app = Flask(__name__)

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