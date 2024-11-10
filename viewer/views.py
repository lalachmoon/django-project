from django.shortcuts import render
from django.http import HttpResponse

from viewer.models import Movie, Genre


# Url parameters cu regular expressions
# def hello(request, s, other_s):
#     return HttpResponse(f'Hello, {s} and {other_s} World!')

# URL Encoding
# def hello(request):
    # print(request.GET)
    # s = request.GET.get('s', '')
    # other_s = request.GET.get('other_s', '')
    # return HttpResponse(f'Hello {s} and {other_s} World!')

# def hello(request):
    # sql WHERE -> .filter()
    # movie1 = Movie.objects.filter(rating=8)

    # Filemele unde genre-ul are numele SciFi
    # genre = Genre.objects.get(name='SciFi')
    # movie2 = Movie.objects.filter(genre=genre)

    # Filmele cu rating mai mare de 8
    # movie3 = Genre.objects.filter(rating__gt=8)

    # .filter() inlantuite
    # movie4 = Movie.objects.filter(title_icontains='godfather').filter(rating=10)

    # cate obiecte sunt in query
    # movie_count = Movie.obejcts.all().count()

    # Varianta 1 de creat un obiect
    # Genre.objects.create(name='Horror')

    # sau varianta 2
    # g = Genre.objects.create(name='Horror')
    # g.save()

    # return HttpResponse('<h1>Filmele mele</h1>')

def home(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    rating = request.GET.get('rating', '')

    if rating != '':
         movies = movies.filter(rating__gt=rating)

    return render(
        request,
        template_name='home.html',
        context={'filme': movies, 'genres': genres}
    )


def film(request, my_slug):
    movie = Movie.objects.get(slug=my_slug)

    return render(
        request,
        template_name='film.html',
        context={'film': movie}
    )


def genre(request, my_slug):
    genre = Genre.objects.get(slug=my_slug)
    movies = Movie.objects.filter(genre=genre)
    all_genres = Genre.objects.all()

    rating = request.GET.get('rating', '')

    if rating != '':
         movies = movies.filter(rating__gt=rating)



    return render(
        request,
        template_name='home.html',
        context={'genres': all_genres, 'filme': movies}
    )


