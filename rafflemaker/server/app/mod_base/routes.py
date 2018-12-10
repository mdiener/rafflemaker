class Routes(object):
    def __init__(self, app, views):
        app.add_url_rule('/rafflemaker/', 'index', views.index)
