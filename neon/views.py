from django.http import HttpResponse
from django.shortcuts import render

import tmdbsimple as tmdb
tmdb.API_KEY = 'bccb4d3a84c5cc22a6e700c100f465f9'


def index(request):
    return render(request, 'index.html')

def films(request):
    return render(request, 'films.html')

def songs(request):
    return render(request, 'songs.html')

def films(request):
    movie = ["","","","",""]

    movie[0] = tmdb.Movies(603)
    response_0 = movie[0].info()
    movie[0].title
    movie[0].budget
    movie[0].genres
    movie[0].homepage
    movie[0].original_language
    movie[0].release_date
    movie[0].runtime
    movie[0].imdb_id


    movie[1] = tmdb.Movies(14467)
    response_1 = movie[1].info()
    movie[1].title
    movie[1].budget
    movie[1].genres
    movie[1].homepage
    movie[1].original_language
    movie[1].release_date
    movie[1].runtime
    movie[1].imdb_id


    movie[2] = tmdb.Movies(5801)
    response_2 = movie[2].info()
    movie[2].title
    movie[2].budget
    movie[2].genres
    movie[2].homepage
    movie[2].original_language
    movie[2].release_date
    movie[2].runtime
    movie[2].imdb_id


    params = {'m1_title': movie[0].title, 'm1_budget': movie[0].budget, 'm1_overview': movie[0].overview, 'm1_poster':movie[0].poster_path, 'm1_genres': list(movie[0].genres[0].values())[1], 'm1_homepage': movie[0].homepage, 'm1_original_language': movie[0].original_language, 'm1_release_date': movie[0].release_date, 'm1_runtime': movie[0].runtime, 'm1_imdb_id': movie[0].imdb_id, 
    'm2_title': movie[1].title, 'm2_budget': movie[1].budget, 'm2_overview': movie[1].overview, 'm2_poster':movie[1].poster_path, 'm2_genres': list(movie[1].genres[0].values())[1], 'm2_homepage': movie[1].homepage, 'm2_original_language': movie[1].original_language, 'm2_release_date': movie[1].release_date, 'm2_runtime': movie[1].runtime, 'm2_imdb_id': movie[1].imdb_id,
    'm3_title': movie[2].title, 'm3_budget': movie[2].budget, 'm3_overview': movie[2].overview, 'm3_poster':movie[2].poster_path, 'm3_genres': list(movie[2].genres[0].values())[1], 'm3_homepage': movie[2].homepage, 'm3_original_language': movie[2].original_language, 'm3_release_date': movie[2].release_date, 'm3_runtime': movie[2].runtime, 'm3_imdb_id': movie[2].imdb_id,}

    return render(request,'films.html',params)

