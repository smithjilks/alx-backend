#!/usr/bin/env python3
""" Simple Flask app """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Languages config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ creates a single / route and an index.html template
    that simply outputs “Welcome to Holberton” """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
