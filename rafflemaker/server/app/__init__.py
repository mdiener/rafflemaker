import os
import flask
from app.mod_base import base
from app.mod_user import user
from app.mod_raffles import raffles

app = flask.Flask(__name__)
app.secret_key = os.urandom(12)


def page_not_found(e):
    return flask.render_template('errors/404.html'), 404


def forbidden(e):
    return flask.render_template('errors/403.html'), 403


def internal_error(e):
    return flask.render_template('errors/500.html'), 500


app.register_error_handler(404, page_not_found)
app.register_error_handler(403, forbidden)
app.register_error_handler(500, internal_error)


base(app)
user(app)
raffles(app)
