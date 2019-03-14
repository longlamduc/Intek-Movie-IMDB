from movies.models import Movie
from celebs.models import Celeb
from awards.models import Award
from django.shortcuts import render

def homeView(request):
    movies = Movie.objects.all()[:3]
    celebs = Celeb.objects.all()[:3]
    awards = Award.objects.all()[:3]
    context = {
        'movies': movies,
        'celebs': celebs,
        'awards': awards,
    }
    return render(request, 'home.html', context=context)