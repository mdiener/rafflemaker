class Routes(object):
    def __init__(self, app, views, rest_views):
        app.add_url_rule('/raffles', 'view.raffles', views.raffles)
        app.add_url_rule('/raffle', 'view.raffle.create', views.create_raffle, methods=['GET', 'POST'])
        app.add_url_rule('/raffle/<int:raffle_id>', 'view.raffle', views.raffle)
        app.add_url_rule('/raffle/<int:raffle_id>/winners', 'view.raffle.winners', views.raffle_winners)
        app.add_url_rule('/rest/raffles', 'rest.raffles', rest_views.raffles)
        app.add_url_rule('/rest/raffle/<int:raffle_id>', 'rest.raffle', rest_views.raffle, methods=['GET', 'POST', 'DELETE'])
        app.add_url_rule('/rest/raffle/<int:raffle_id>/winners', 'rest.raffle.winners', rest_views.raffle_winners, methods=['GET'])
        app.add_url_rule('/rest/raffle/<int:raffle_id>/last-winners', 'rest.raffle.last_winners', rest_views.raffle_last_winners, methods=['GET'])
        app.add_url_rule('/rest/raffle/<int:raffle_id>/contestant', 'rest.raffle.contestant.create', rest_views.create_contestant, methods=['POST'])
        app.add_url_rule('/rest/raffle/<int:raffle_id>/contestant/<int:contestant_id>', 'rest.raffle.contestant', rest_views.contestant, methods=['POST', 'DELETE'])
        app.add_url_rule('/rest/raffle/<int:raffle_id>/contestants', 'rest.raffle.contestants', rest_views.contestants)
