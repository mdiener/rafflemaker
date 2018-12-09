import flask


class Views(object):
    def index(self):
        if 'userdata' in flask.session:
            return flask.redirect(flask.url_for('view.raffles'))

        return flask.render_template('mod_base/index.html')
