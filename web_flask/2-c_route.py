#!/usr/bin/python3
""" Script starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    the function serving the root/home page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    the function serves hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    the function displays /c/<text>
    """
    neu_text = text.replace('_', ' ')
    return "C {}".format(neu_text)


if __name__ == "__main__":
    """
     Runs FLask only when script is executed directly.
    Executed only if the Python script is run
    directly, not imported as a module.
    It starts Flask, & allows external access.
    """
    app.run(host="0.0.0.0", port=5000)
