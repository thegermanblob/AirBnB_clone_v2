#!/usr/bin/env python3
from flask import Flask
from flask.scaffold import F
""" flask app dlepoyer"""
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ prints hello """
    return 'Hello HBNB!'
