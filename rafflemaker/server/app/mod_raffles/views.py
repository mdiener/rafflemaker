import flask
from app.mod_raffles import raffle
from app.mod_raffles.exceptions import RaffleCreationError, RaffleNotFoundError, RaffleError, RaffleAlreadyExistsError


class Views(object):
    def raffles(self):
        if 'userdata' not in flask.session:
            return flask.abort(403)

        return flask.render_template('mod_raffles/raffles.html')

    def raffle(self, raffle_id):
        if 'userdata' not in flask.session:
            return flask.abort(403)

        try:
            raffle.get_raffle(flask.session['userdata']['userid'], raffleid=raffle_id)
        except (RaffleNotFoundError, RaffleError) as e:
            flask.flash(str(e))
            return flask.redirect(flask.url_for('view.raffles'))

        return flask.render_template('mod_raffles/raffle.html')

    def raffle_winners(self, raffle_id):
        if 'userdata' not in flask.session:
            return flask.abort(403)

        try:
            raffle.get_raffle(flask.session['userdata']['userid'], raffleid=raffle_id)
        except (RaffleNotFoundError, RaffleError) as e:
            flask.flash(str(e))
            return flask.redirect(flask.url_for('view.raffles'))

        return flask.render_template('mod_raffles/winners.html')

    def create_raffle(self):
        if 'userdata' not in flask.session:
            return flask.abort(403)

        if flask.request.method == 'POST':
            if 'name' not in flask.request.form and 'max_winners' not in flask.request.form:
                flask.flash('You need to provide at least a name and the maximum number of winners for a raffle.')
                return flask.redirect(flask.url_for('view.raffle.create'))

            name = flask.request.form['name']
            max_winners = flask.request.form['max_winners']
            description = flask.request.form['description']

            try:
                raffleid = raffle.create(name, flask.session['userdata']['userid'], description=description, max_winners=max_winners)
            except (RaffleCreationError, RaffleAlreadyExistsError) as e:
                flask.flash(str(e))
                return flask.render_template('mod_raffles/create_raffle.html')

            return flask.redirect(flask.url_for('view.raffle', raffle_id=raffleid))
        else:
            return flask.render_template('mod_raffles/create_raffle.html')
