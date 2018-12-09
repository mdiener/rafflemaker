import time
import uuid
import crypt
import hashlib
from hmac import compare_digest as compare_hash
import app.mod_user.exceptions
from app.sql import SQLConnector


def get_user(email=None, userid=None):
    sql = SQLConnector()

    if userid is not None:
        user = sql.query_get_one('SELECT * FROM user WHERE id=?', (userid,))
    elif email is not None:
        user = sql.query_get_one('SELECT * FROM user WHERE email=?', (email,))

    if user is None:
        raise app.mod_user.exceptions.UserNotFoundError('Could not find the user requested.')

    return user


def do_login(email, password):
    sql = SQLConnector()
    user = sql.query_get_one('SELECT * FROM user WHERE email=?', (email,))

    if user is None:
        raise app.mod_user.exceptions.UserNotFoundError('Could not find the user with the email address ' + email)

    if not compare_hash(user['password'], crypt.crypt(password, user['password'])):
        raise app.mod_user.exceptions.CredentialsInvalidError('Could not verify the credentials provided. Please try again.')


def create(email, password, name):
    if email_exists(email):
        raise app.mod_user.exceptions.UserAlreadyExistsError('The provided email already exists. Please log in or chose a new one.')

    sql = SQLConnector()

    created = int(time.time())
    userid = uuid.uuid4().hex
    password = crypt.crypt(password)

    sql.query_insert('INSERT INTO user(email, password, created, name) VALUES (?, ?, ?, ?)', (email, password, created, name))


def update_password(userid, old_password, new_password):
    sql = SQLConnector()

    user = sql.query_get_one('SELECT * FROM user WHERE id=?', (userid,))
    if user is None:
        raise app.mod_user.exceptions.UserNotFoundError('Could not find the user with userid ' + userid)

    if not compare_hash(user['password'], crypt.crypt(old_password, user['password'])):
        raise app.mod_user.exceptions.CredentialsInvalidError('Could not verify the old password, please try again.')

    new_password = crypt.crypt(new_password)
    sql.query_update('UPDATE user SET password=? WHERE id=?', (new_password, userid,))


def new_password(userid, password):
    sql = SQLConnector()

    try:
        get_user(userid=userid)
    except app.mod_user.exceptions.UserNotFoundError as e:
        raise e

    password = crypt.crypt(password)

    sql.query_update('UPDATE user SET password=? WHERE id=?', (password, userid, ))


def email_exists(email):
    sql = SQLConnector()
    user = sql.query_get_one('SELECT * FROM user WHERE email=?', (email, ))

    if user is not None:
        return True

    return False


def create_reset_link(email=None, userid=None):
    sql = SQLConnector()

    if email is not None:
        userid = get_user(email=email)['id']

    hash = hashlib.sha256(uuid.uuid4().bytes).hexdigest()

    try:
        get_user_resetlink(userid=userid)
        sql.query_update('UPDATE user_resetlink SET hash=?', (hash, ))
    except app.mod_user.exceptions.UserResetLinkNotExists as e:
        sql.query_insert('INSERT INTO user_resetlink(hash, user_id) VALUES(?, ?)', (hash, userid, ))

    return hash


def remove_reset_link(userid=None):
    sql = SQLConnector()

    get_user_resetlink(userid=userid)
    sql.query_delete('DELETE FROM user_resetlink WHERE user_id=?', (userid, ))


def get_user_resetlink(userid=None, hash=None):
    sql = SQLConnector()

    if userid is not None:
        user_resetlink = sql.query_get_one('SELECT * FROM user_resetlink WHERE user_id=?', (userid, ))
    elif hash is not None:
        user_resetlink = sql.query_get_one('SELECT * FROM user_resetlink WHERE hash=?', (hash, ))

    if user_resetlink is None:
        raise app.mod_user.exceptions.UserResetLinkNotExists('Could not find a reset link associated with this hash or userid.')
    else:
        return user_resetlink
