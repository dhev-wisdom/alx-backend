#!/usr/bin/env python3
"""
Moldule setup a basic flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Home route"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
