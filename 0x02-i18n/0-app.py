#!/usr/bin/env python3
"""
Flask app module
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Route for the index page.
    """
    title = "Welcome to Holberton"
    header = "Hello world"

    return render_template('0-index.html', title=title, header=header)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
