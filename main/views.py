from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Films, FilmSeries, FilmGenre
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug(request, single_slug):
    genres = [g.genre_slug for g in FilmGenre.objects.all()]
    if single_slug in genres:
        matching_series = FilmSeries.objects.filter(film_genre__genre_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Films.objects.filter(film_series__film_series=m.film_series).earliest("review_published")
            series_urls[m] = part_one.film_slug

        return render(request,
                      template_name='main/genre.html',
                      context={'film_series': matching_series, 'part_ones': series_urls})

    films = [f.film_slug for f in Films.objects.all()]
    if single_slug in films:
        this_film = Films.objects.get(film_slug = single_slug)
        films_from_series = Films.objects.filter(film_series__film_series=this_film.film_series).order_by('review_published')
        this_film_idx = list(films_from_series).index(this_film)

        return render(request,
                      'main/film.html',
                      {'film': this_film,
                       'sidebar': films_from_series,
                       'this_fil_idx': this_film_idx})

    return HttpResponse(f"{single_slug} does nor corresponds to anything.")


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/genres.html',
                  context={"genres": FilmGenre.objects.all})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created :{username}")
            login(request, user)
            return redirect('main:homepage')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request,
                  template_name='main/register.html',
                  context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged Out Successfully!!')
    return redirect('main:homepage')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request = request,
                  template_name = 'main/login.html',
                  context = {'form': form})
