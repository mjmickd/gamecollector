from django.shortcuts import render

#baby step - Usually a Model is used instead 
games = [
  {'name': 'Mario Kart 8 Deluxe', 'system': 'Nintendo Switch', 'description': 'racing game with fun tricks and twists', 'released': 2017},
  {'name': 'Luigi''s Mansion', 'system': 'Nintendo Gamecube', 'description': 'ghostbusters meets Nintendo', 'released': 2003},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {
        'games': games
    })