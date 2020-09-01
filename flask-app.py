import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('states-data.json', 'r') as statesFile:
    states=json.load(statesFile)

@app.route('/states.json')
def states_():
    return states