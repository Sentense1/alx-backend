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
    home_title = "Welcome to Holberton"
    home_header = "Hello world"

    return render_template('0-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
