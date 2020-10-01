from django.db import models
from sleeper_wrapper import League

league_id = '553670046391185408'

league = League(league_id)

class getLeagueUsers()
    leagueUsers = league.get_user()
    return render_to_response('home/home_data.html', leagueUsers)
