class Routes(object):
    def __init__(self, app, views):
        app.add_url_rule('/user', 'view.user', views.user)
        app.add_url_rule('/user/login', 'view.login', views.login, methods=['POST'])
        app.add_url_rule('/user/logout', 'view.logout', views.logout)
        app.add_url_rule('/user/create', 'view.user.create', views.create_user, methods=['GET', 'POST'])
        app.add_url_rule('/user/reset-password', 'view.user.resetpw', views.reset_password, methods=['GET', 'POST'])
        app.add_url_rule('/user/reset-link', 'view.user.resetlink', views.reset_link, methods=['GET', 'POST'])
