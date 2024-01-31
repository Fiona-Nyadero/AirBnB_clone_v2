#!/usr/bin/python3
""" Script starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    the function serves the root/home page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    the function serves the hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    the function displays /c/<text>
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    the function displays /python/<text>>
    """
    neu_text = text.replace('_', ' ')
    return "Python {}".format(neu_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_only(n):
    """
    the function displays numbers only
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    the function displays a number template
    using rendering template
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    """
    Runs FLask only when script is executed directly.
    Executed only if the Python script is run
    directly, not imported as a module.
    It starts Flask, & allows external access.
    """
    app.run(host="0.0.0.0", port=5000)
