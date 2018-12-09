import flask
from app.mod_base import views, routes


def base(app):
    view = views.Views()
    route = routes.Routes(app, view)
