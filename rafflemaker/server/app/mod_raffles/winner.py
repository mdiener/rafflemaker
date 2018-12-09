import random
import time
from app.sql import SQLConnector
from app.mod_raffles import contestant
from app.mod_raffles import raffle


def select_winners(raffleid, userid):
    sql = SQLConnector()
    rand = random.SystemRandom()

    contestants = contestant.get_all(raffleid, userid)
    max_winners = raffle.get_raffle(userid, raffleid=raffleid)['max_winners']

    winner_list = []
    for entry in contestants:
        for i in range(entry['entries']):
            winner_list.append({
                'id': entry['id'],
                'name': entry['name']
            })

    random.shuffle(winner_list)
    winners = []

    for i in range(max_winners):
        winner = winner_list[rand.randint(0, len(winner_list))]
        winner_list = [cont for cont in winner_list if cont['id'] != winner['id']]

        winners.append(winner)

    timestamp = int(time.time())

    for winner in winners:
        sql.query_insert('INSERT INTO winner(timestamp, contestant_id, raffle_id, user_id) VALUES(?, ?, ?, ?)', (timestamp, winner['id'], raffleid, userid, ))

    return winners


def get_last_winners(raffleid, userid):
    sql = SQLConnector()

    all_winners = sql.query_get_all('SELECT * FROM winner WHERE raffle_id=? AND user_id=? ORDER BY timestamp DESC', (raffleid, userid, ))
    last_timestamp = all_winners[0]['timestamp']
    last_winners = []
    for winner in all_winners:
        if winner['timestamp'] == last_timestamp:
            last_winners.append({'id': winner['contestant_id']})

    return last_winners
