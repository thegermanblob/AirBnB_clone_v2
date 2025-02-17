#!/usr/bin/python3
""" flask app deployer module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function prints hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
