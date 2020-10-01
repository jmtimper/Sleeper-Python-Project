from django.http import HttpResponse
# from sleeper_wrapper import League

# league_id = '553670046391185408'

# league = League(league_id)

def index(request):
    
    return HttpResponse("Hello, world. You're at the polls index." + leagueUsers)