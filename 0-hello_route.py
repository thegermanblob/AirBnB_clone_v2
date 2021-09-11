#!/usr/bin/env python3
from flask import Flask
from flask.scaffold import F

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'