#!/usr/bin/env python3
"""
Flask app module
"""
from flask_babel import Babel
from flask_babel import gettext as _
from flask import Flask, render_template, request


# Instantiate the Flask app
app = Flask(__name__)
# Instantiate the  Babel object and store it in a module-level variable.
babel = Babel(app)


# Define a config class
class Config(object):
    """
    Config class for multi languages
    """
    # class attr with languages to support
    LANGUAGES = ["en", "fr"]
    # default language for browser
    BABEL_DEFAULT_LOCALE = "en"
    # default timezone for browser
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the Config to flask app after setting the Config class
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """
    Route for the index page
    """
    return render_template('3-index.html')


# define a function that selects the appropriate locale (language)
@babel.localeselector
def get_locale() -> str:
    """
    Returns the best match for support languages
    """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

