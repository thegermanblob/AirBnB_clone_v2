#!/usr/bin/python3
""" flask app dlepoyer"""
from flask import Flask
from flask.scaffold import F
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ prints hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
