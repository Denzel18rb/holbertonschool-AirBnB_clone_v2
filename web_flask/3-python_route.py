#!/usr/bin/python3
"""Script that starts a Flask web with 4 routes"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hi_route():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    text = text.replace("_", " ")
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
