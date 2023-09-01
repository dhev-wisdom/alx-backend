#!/usr/bin/env python3
"""
Moldule setup a basic flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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
    local = request.args.get("locale", None)
    if locale and locale in apps.config{"LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """Home route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
