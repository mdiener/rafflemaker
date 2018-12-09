from app.sql import SQLConnector
from app.mod_raffles.exceptions import RaffleCreationError, RaffleNotFoundError, RaffleError, RaffleAlreadyExistsError, RaffleParameterError


def create(name, userid, description='', max_winners=1):
    sql = SQLConnector()

    if not isinstance(name, str) or len(name) < 5:
        raise RaffleCreationError('The name of the raffle needs to be at least 5 characters long.')

    if _exists(userid, name=name):
        raise RaffleAlreadyExistsError('The raffle already exists.')

    sql.query_insert('INSERT INTO raffle(name, description, max_winners, user_id) VALUES (?, ?, ?, ?)', (name, description, max_winners, userid,))

    raffle = get_raffle(name=name, userid=userid)
    return raffle['id']


def update(name, description, max_winners, raffleid, userid):
    sql = SQLConnector()

    if not isinstance(name, str) or len(name) < 5 or not isinstance(description, str) or not isinstance(max_winners, int):
        raise RaffleParameterError('The name needs to be a string of at least 5 characters. The description needs to a string and the max_winners needs to be an int.')

    if not _exists(userid, raffleid=raffleid):
        raise RaffleNotFoundError('The raffle could not be found.')

    sql.query_update('UPDATE raffle SET name=?, description=?, max_winners=? WHERE id=? AND user_id=?', (name, description, max_winners, raffleid, userid))


def delete(raffleid, userid):
    sql = SQLConnector()

    if not _exists(userid, raffleid=raffleid):
        raise RaffleNotFoundError('The raffle could not be found.')

    sql.query_delete('DELETE FROM raffle WHERE id=? AND user_id=?', (raffleid, userid))


def _exists(userid, **kwargs):
    try:
        get_raffle(userid, **kwargs)
    except RaffleNotFoundError:
        return False

    return True


def get_raffle(userid, **kwargs):
    sql = SQLConnector()
    raffle = None

    if 'name' in kwargs:
        raffle = sql.query_get_one('SELECT * FROM raffle WHERE name=? AND user_id=?', (kwargs['name'], userid,))
    elif 'raffleid' in kwargs:
        raffle = sql.query_get_one('SELECT * FROM raffle WHERE id=? AND user_id=?', (kwargs['raffleid'], userid,))
    else:
        raise RaffleError('Need to have either name and userid or the raffleid to retrieve a raffle.')

    if raffle is None:
        raise RaffleNotFoundError('The raffle could not be found in your raffles.')

    return raffle


def get_all(userid):
    sql = SQLConnector()
    return sql.query_get_all('SELECT * FROM raffle WHERE user_id=?', (userid,))
