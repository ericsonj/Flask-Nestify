from flask import Flask
from flask_nestify import Nestpy

app = Flask(__name__)
Nestpy(app)
