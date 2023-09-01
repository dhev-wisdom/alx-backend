#!/usr/bin/env python3
"""
Moldule setup a basic flask app
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Set locale language"""
    return app.config["BABEL_DEFAULT_LOCALE"]


@app.route("/", strict_slashes=False)
def index():
    """Home route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
