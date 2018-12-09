import json
import flask
from app.mod_raffles import raffle
from app.mod_raffles import contestant
from app.mod_raffles import winner
from app.mod_raffles.exceptions import RaffleNotFoundError, RaffleError, ContestantError, ContestantAlreadyExistsError, ContestantNotFoundError, ContestantParameterError, RaffleParameterError


def not_found_error(message):
    return json.dumps({
        'error': 404,
        'name': 'Not Found',
        'message': message
    }), 404


def forbidden_error(message):
    return json.dumps({
        'error': 403,
        'name': 'Forbidden',
        'message': message
    }), 403


def bad_request_error(message):
    return json.dumps({
        'error': 400,
        'name': 'Bad Request',
        'message': message
    }), 400


def internal_server_error(message):
    return json.dumps({
        'error': 500,
        'name': 'Internal Server Error',
        'message': message
    }), 500


class RestViews(object):
    def raffles(self):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        result = raffle.get_all(flask.session['userdata']['userid'])
        list = []

        for row in result:
            list.append({
                'name': row['name'],
                'raffleid': row['id'],
                'description': row['description'],
                'max_winners': row['max_winners']
            })

        return json.dumps(list)

    def raffle(self, raffle_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        if flask.request.method == 'GET':
            try:
                raffledata = raffle.get_raffle(flask.session['userdata']['userid'], raffleid=raffle_id)
            except RaffleNotFoundError as e:
                return not_found_error(str(e))

            return json.dumps({
                'name': raffledata['name'],
                'description': raffledata['description'],
                'max_winners': raffledata['max_winners']
            })
        elif flask.request.method == 'POST':
            data = flask.request.get_json()
            if 'name' not in data or 'description' not in data or 'max_winners' not in data:
                return bad_request_error('Name, description and max_winners are required fields.')

            try:
                raffle.update(data['name'], data['description'], data['max_winners'], raffle_id, flask.session['userdata']['userid'])
            except RaffleParameterError as e:
                return bad_request_error(str(e))
            except RaffleNotFoundError as e:
                return not_found_error(str(e))

            return json.dumps({
                'name': data['name'],
                'description': data['description'],
                'max_winners': data['max_winners']
            })
        elif flask.request.method == 'DELETE':
            try:
                raffle.delete(raffle_id, flask.session['userdata']['userid'])
            except RaffleNotFoundError as e:
                return not_found_error(str(e))

            return json.dumps({})

    def raffle_last_winners(self, raffle_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        winners = winner.get_last_winners(raffle_id, flask.session['userdata']['userid'])
        return json.dumps(winners)

    def raffle_winners(self, raffle_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        winners = winner.select_winners(raffle_id, flask.session['userdata']['userid'])
        return json.dumps(winners)

    def contestant(self, raffle_id, contestant_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        if flask.request.method == 'POST':
            data = flask.request.get_json()
            if 'name' not in data or 'tickets' not in data:
                return bad_request_error('Name and tickets need to be set.')

            try:
                contestant.update(data['name'], data['tickets'], contestant_id, raffle_id, flask.session['userdata']['userid'])
            except ContestantNotFoundError as e:
                return not_found_error(str(e))
            except ContestantParameterError as e:
                return internal_server_error(str(e))

        elif flask.request.method == 'DELETE':
            try:
                contestant.delete(raffle_id, contestant_id, flask.session['userdata']['userid'])
            except ContestantNotFoundError as e:
                return not_found_error(str(e))

        return json.dumps({})

    def create_contestant(self, raffle_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        data = flask.request.get_json()
        if 'name' not in data or 'tickets' not in data:
            return bad_request_error('Name and tickets needs to be set.')

        try:
            contestant.create(data['name'], data['tickets'], raffle_id, flask.session['userdata']['userid'])
        except (ContestantParameterError, ContestantAlreadyExistsError) as e:
            return bad_request_error(str(e))

        return json.dumps({})

    def contestants(self, raffle_id):
        if 'userdata' not in flask.session:
            return forbidden_error('')

        result = contestant.get_all(raffle_id, flask.session['userdata']['userid'])
        list = []

        for row in result:
            list.append({
                'contestantid': row['id'],
                'name': row['name'],
                'tickets': row['entries']
            })

        return json.dumps(list)
