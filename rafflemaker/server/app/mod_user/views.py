import flask
from app.mod_user import user
import app.mod_user.exceptions
from app.mod_user.email import Email


class Views(object):
    def login(self):
        if 'email' in flask.session:
            return flask.redirect(flask.url_for('index'))

        if 'email' not in flask.request.form and 'password' not in flask.request.form:
            flask.flash('You need to provide a username and password to log in.')
            return flask.redirect(flask.url_for('view.login'))

        email = flask.request.form['email']
        password = flask.request.form['password']

        try:
            user.do_login(email, password)
        except (app.mod_user.exceptions.CredentialsInvalidError, app.mod_user.exceptions.UserNotFoundError) as e:
            flask.flash(str(e))
            return flask.redirect(flask.url_for('index'))

        userdata = user.get_user(email=email)

        flask.session['userdata'] = {
            'email': userdata['email'],
            'userid': userdata['id'],
            'name': userdata['name']
        }

        return flask.redirect(flask.url_for('view.raffles'))

    def logout(self):
        if 'userdata' in flask.session:
            flask.session.pop('userdata', None)

        return flask.redirect(flask.url_for('index'))

    def user(self):
        if 'userdata' not in flask.session:
            return flask.abort(403)

        return flask.render_template('mod_user/user.html', name=flask.session['userdata']['name'], email=flask.session['userdata']['email'])

    def create_user(self):
        if 'userdata' in flask.session:
            return flask.redirect(flask.url_for('index'))

        if flask.request.method == 'POST':
            if 'email' not in flask.request.form and 'password' not in flask.request.form and 'name' not in flask.request.form:
                flask.flash('You need to provide an email, password and name to create a new account.')
                return flask.redirect(flask.url_for('user.create'))

            email = flask.request.form['email']
            password = flask.request.form['password']
            name = flask.request.form['name']

            try:
                user.create(email, password, name)
            except app.mod_user.exceptions.UserAlreadyExistsError as e:
                flask.flash(str(e))
                return flask.render_template('mod_user/user.html')

            flask.flash('Your user has been created. You can now log in and start your raffles!')
            return flask.redirect(flask.url_for('index'))
        else:
            return flask.render_template('mod_user/create_user.html')

    def reset_password(self):
        if flask.request.method == 'POST':
            if 'email' not in flask.request.form:
                flask.flash('You need to provide an email.')
                return flask.render_template('mod_user/reset_password.html')

            try:
                u = user.get_user(email=flask.request.form['email'])
            except app.mod_user.exceptions.UserNotFoundError as e:
                flask.flash(str(e))
                return flask.render_template('mod_user/reset_password.html')

            hash_link = user.create_reset_link(userid=u['id'])

            email = Email()
            email.send_reset_email(u['name'], flask.request.form['email'], hash_link)

            flask.flash('Your password reset link has been sent to ' + flask.request.form['email'])
            return flask.redirect(flask.url_for('index'))
        elif flask.request.method == 'GET':
            return flask.render_template('mod_user/reset_password.html')

    def reset_link(self):
        if flask.request.method == 'POST':
            if 'hash' not in flask.request.form or 'password' not in flask.request.form:
                return flask.abort(403)

            try:
                user_resetlink = user.get_user_resetlink(hash=flask.request.form['hash'])
            except app.mod_user.exceptions.UserResetLinkNotExists as e:
                flask.flash('Please try resetting your password again and make sure the link is sent to you properly.')
                flask.abort(403)

            try:
                user.new_password(user_resetlink['user_id'], flask.request.form['password'])
            except app.mod_user.exceptions.UserNotFoundError as e:
                flask.flash(str(e))
                flask.abort(403)

            user.remove_reset_link(user_resetlink['user_id'])

            flask.flash('Your new password has been set, you can now log in.')
            return flask.redirect(flask.url_for('index'))

        elif flask.request.method == 'GET':
            if 'hash' not in flask.request.args:
                return flask.abort(403)

            hash = flask.request.args['hash']
            try:
                user_resetlink = user.get_user_resetlink(hash=hash)
            except app.mod_user.exceptions.UserResetLinkNotExists as e:
                flask.flash('Please try resetting your password again and make sure the link is sent to you properly.')
                return flask.abort(403)

            return flask.render_template('mod_user/reset_link.html', hash=hash)
