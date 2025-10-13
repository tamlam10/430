from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

from django.shortcuts import render

def list_movies(request):
    movies = Movie.objects.all().order_by("MovieTitle")
    return render(request, "movies1/list_movies.html", {"movies": movies})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        form = MovieForm()
    return render(request, 'movies1/add_movie.html', {'form': form})

def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies1/edit_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('list_movies')
    return render(request, 'movies1/delete_movie.html', {'movie': movie})
