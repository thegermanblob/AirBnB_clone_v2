#!/usr/bin/python3
""" flask app deployer module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function prints hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function prints hbnb"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ returns c with added text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ returns python with added text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returns n is a number if is a number """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
