from app.sql import SQLConnector
from app.mod_raffles.exceptions import ContestantNotFoundError, ContestantAlreadyExistsError, ContestantError, ContestantParameterError, ContestantNotFoundError


def update(name, tickets, contestantid, raffleid, userid):
    sql = SQLConnector()

    if not isinstance(name, str) or len(name) < 4:
        raise ContestantParameterError('Name has to be a string with at least 3 characters.')

    if not isinstance(tickets, int) or tickets < 0:
        raise ContestantParameterError('Tickets have to be a minimum of 0.')

    if not _exists(raffleid, userid, contestantid=contestantid):
        raise ContestantNotFoundError('The contestant you tried to edit does not exist.')

    sql.query_update('UPDATE contestant SET name=?, entries=? WHERE id=?', (name, tickets, contestantid))


def create(name, tickets, raffleid, userid):
    sql = SQLConnector()

    if not isinstance(name, str) or len(name) < 4:
        raise ContestantParameterError('Name has to be a string with at least 3 characters.')

    if not isinstance(tickets, int) or tickets < 0:
        raise ContestantParameterError('Tickets have to be a minimum of 0.')

    if _exists(raffleid, userid, name=name):
        raise ContestantAlreadyExistsError('The contestant with the name ' + name + ' already exists. Please edit the contestant in the list or delete it first to add a new entry for this name.')

    sql.query_insert('INSERT INTO contestant(name, entries, autowin, raffle_id, user_id) VALUES(?, ?, ?, ?, ?)', (name, tickets, 0, raffleid, userid))


def delete(raffleid, contestantid, userid):
    sql = SQLConnector()

    if not _exists(raffleid, userid, contestantid=contestantid):
        raise ContestantNotFoundError('Could not find the contestant.')

    sql.query_delete('DELETE FROM contestant WHERE id=? AND raffle_id=? AND user_id=?', (contestantid, raffleid, userid))


def _exists(raffleid, userid, **kwargs):
    sql = SQLConnector()

    if 'name' in kwargs:
        contestant = sql.query_get_one('SELECT * FROM contestant WHERE name=? AND raffle_id=? AND user_id=?', (kwargs['name'], raffleid, userid,))
    elif 'contestantid' in kwargs:
        contestant = sql.query_get_one('SELECT * FROM contestant WHERE id=? AND raffle_id=? and user_id=?', (kwargs['contestantid'], raffleid, userid))
    else:
        return False

    if contestant is not None:
        return True

    return False


def get_all(raffleid, userid):
    sql = SQLConnector()

    return sql.query_get_all('SELECT * FROM contestant WHERE raffle_id=? AND user_id=?', (raffleid, userid,))
