from flask import Flask
from flask_cors import CORS, cross_origin
#INITIATING API
app = Flask(__name__)
CORS(app)