import flask
from app.mod_raffles import views, routes, rest_views


def raffles(app):
    view = views.Views()
    rest_view = rest_views.RestViews()
    route = routes.Routes(app, view, rest_view)
