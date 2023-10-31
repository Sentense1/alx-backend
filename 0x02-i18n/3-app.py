#!/usr/bin/env python3
"""
Flask app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


# Define a config class
class Config:
    """
    Config class for multi languages
    """
    # class attr with languages to support
    LANGUAGES = ["en", "fr"]
    # default language for browser
    BABEL_DEFAULT_LOCALE = "en"
    # default timezone for browser
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the Flask app
app = Flask(__name__)
# Instantiate the  Babel object and store it in a module-level variable.
babel = Babel(app)
app.url_map.strict_slashes = False

# Apply the Config to flask app after setting the Config class
app.config.from_object(Config)


# define a function that selects the appropriate locale (language)
@babel.localeselector
def get_locale():
    """
    Returns the best match for support languages
    """
    return request.accept_languages.best_match(app.config.LANGUAGES)


@app.route('/')
def index():
    """
    Route for the index page
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
