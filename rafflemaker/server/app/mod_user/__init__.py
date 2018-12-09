import flask
from app.mod_user import views, routes


def user(app):
    view = views.Views()
    route = routes.Routes(app, view)
