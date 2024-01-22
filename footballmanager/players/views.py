from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Player

# Create your views here.
def players(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def scout(request):
    countries = ['England', 'Hungary', 'Norway']

    players = []
    features = []
    filtered = False
    selected = ""
    feature = 'name'
    country = ""

    if request.method == 'POST':
        country = request.POST.get('nationality')
        feature = request.POST.get('feature')
        players = Player.objects.filter(nationality=country)
        players_static = []
        for p in players:
            players_static.append({
                'name': p.name,
                'age': p.age,
                'defense': p.get_defence(),
                'midfield': p.get_midfield(),
                'attack': p.get_attack(),
                'condition': p.condition,
                'injured': p.injured
            })
        filtered = True
        selected = country
        features = list(players_static[0])
        if feature is not None:
            players_static = sorted(players_static, key=lambda x: x[feature], reverse=True)
        players = players_static

    template = loader.get_template('scout.html')
    # at kell alakitani olyan formara amit a html igenyel
    context = {
        'players': players,
        'countries': countries,
        'country': country,
        'features': features,
        'filtered': filtered,
        'selected': selected
    }
    return HttpResponse(template.render(context, request))

def test(request):
    mydata = Player.objects.filter(nationality='England')
    template = loader.get_template('template.html')
    context = {
        'players': mydata,
    }

    return HttpResponse(template.render(context, request))
