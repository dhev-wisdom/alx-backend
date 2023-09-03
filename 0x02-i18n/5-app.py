#!/usr/bin/env python3
"""
Moldule setup a basic flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Set locale language"""
    locale = request.args.get("locale", None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    function that returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    login_user = request.args.get("login_as", None)

    if login_user is None:
        return None

    user = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]

@app.before_request
def before_request():
    """Fo find a user if any, and set it as a global"""
    g.user = str(get_user())

@app.route("/", strict_slashes=False)
def index():
    """Home route"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
