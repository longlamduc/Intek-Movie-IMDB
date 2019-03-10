from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# Create your views here.
def movie(request):
    return render(request, 'movies/movie.html', {'movie_list': Movie.objects.all()})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if Movie.objects.filter(title = title).count() != 0:
                raise ValidationError('This movie existed')
            movie = form.save(commit=False)
            if movie.logo == "":
                movie.logo = "abc"
            if movie.trailer == "":
                movie.trailer = "abc"
            movie.save()
            form.save_m2m()
            return redirect('movie')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def edit_movie(request, movie_id=None):
    item = get_object_or_404(Movie, id=movie_id)
    form = MovieForm(request.POST or None, instance=item)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.save()
        form.save_m2m()
        # Movie.objects.filter(id=movie_id).delete()
        return redirect('movie')
    return render(request, 'movies/movie_form.html', {'form': form})

def delete_movie(request, movie_id=None):
    Movie.objects.get(id=movie_id).delete()
    return redirect('movie')
