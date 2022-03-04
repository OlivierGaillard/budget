from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)

@app.route("/")
def hello():
    return "Salut Mika!"
