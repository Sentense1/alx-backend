#!/usr/bin/env python3
'''
    Use Babel to get user locale.
'''
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Optional

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    '''
        Babel configuration.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    '''
        Get user from session as per variable.
    '''
    user_id = request.args.get('login_as')
    if not user_id:
        return
    try:
        user = users.get(int(user_id))
        if request.args.get('locale'):
            user['locale'] = request.args.get('locale')
        return user
    except Exception:
        return


@app.before_request
def before_request():
    '''
        Operations before request.
    '''
    g.user = get_user()


@app.route('/', strict_slashes=False)
def helloWorld() -> str:
    '''
        Render template for Babel usage.
    '''
    if g.user:
        username = g.user.get('name')
    else:
        username = None
    return render_template('5-index.html', username=username)


@babel.localeselector
def get_locale() -> str:
    '''
        Get user locale to serve matching translation.
    '''
    user = g.user
    if user and 'locale' in user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
