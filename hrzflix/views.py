from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .form import CustomUserForm 
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import json

def home(request):
    trending_movie = Movie.objects.filter(trending=1).order_by('?')[:6]
    movies = Movie.objects.filter(theme__name="Movie").order_by('?')[:6]
    slider1 = Slider.objects.all().order_by('?')[:4]
    slider2 = Slider.objects.exclude(id__in=[slider.id for slider in slider1]).order_by('?')[:4]
    animes = Movie.objects.filter(theme__name="Anime").order_by("?")[:6]
    series = Movie.objects.filter(theme__name="Series").order_by("?")[:6]
    return render(request,'app/index.html',{'trending_movie':trending_movie,"movies":movies,"animes":animes,"series":series,'slider1': slider1,'slider2':slider2})



def movies(request):
    

    movies = Movie.objects.filter(theme__name="Movie")
    genres = Genre.objects.all()

    genre_id = int(request.GET.get('genre')) if request.GET.get('genre') else None
    search_query = request.GET.get('search')

    if search_query:
        movies = movies.filter(Q(name__icontains=search_query) | Q(genre__name__icontains = search_query))
    
    if genre_id:
        movies = movies.filter(genre_id=genre_id)

    paginator = Paginator(movies,8)

    page_num = request.GET.get('page')

    movies = paginator.get_page(page_num)

    return render(request, "app/movies.html", {"movies": movies, "genres": genres, "genre_id": genre_id})


def animes(request):
    animes = Movie.objects.filter(theme__name="Anime")
    genres =Genre.objects.all()

    genre_id = int(request.GET.get('genre')) if request.GET.get('genre') else None
    search_query = request.GET.get('search')

    if search_query:
        animes = animes.filter(Q(name__icontains = search_query) | Q(genre__name__icontains = search_query))
    if genre_id:
        animes = animes.filter(genre_id=genre_id)

    paginator = Paginator(animes, 8)

    page_number = request.GET.get('page')

    animes = paginator.get_page(page_number)    

    return render(request,"app/animes.html",{"animes":animes,"genres":genres,"genre_id":genre_id})


def series(request):
    series = Movie.objects.filter(theme__name="Series")
    genres = Genre.objects.all()

    genre_id = int(request.GET.get('genre')) if request.GET.get('genre') else None
    search_query = request.GET.get('search')

    if search_query:        
        series = series.filter(Q(name__icontains = search_query) | Q(genre__name__icontains = search_query))


    if genre_id:
        series = series.filter(genre_id=genre_id)

    paginator = Paginator(series, 8)  

    page_number = request.GET.get('page')

    series = paginator.get_page(page_number)    

    return render(request,"app/series.html",{"genres":genres,"series":series,"genre_id":genre_id})



def movie_details(request, name):
    movie = Movie.objects.get(name=name)
    genre = Genre.objects.all()
    themes = Theme.objects.all()
    
    related_movies = Movie.objects.filter(
        Q(genre=movie.genre),
        Q(theme=movie.theme),
    ).exclude(name=movie.name).order_by('?')[:6]
    
    context={
            "movie": movie, 
            "genres": genre, 
            "themes": themes, 
            "related_movies": related_movies,
    }
    return render(request, "app/details.html", context)

def trailer_view(request, name):
    movie = Movie.objects.get(name=name)
    trailer_url = movie.trailer_url
    context = {
        "trailer_url": trailer_url,
    }
    return render(request, "app/trailer.html", context)

def trailer_view_2(request,name):
    slider_movie = Slider.objects.get(name=name)
    trailer_url = slider_movie.trailer_url
    context = {
        "trailer_url_2": trailer_url,
    }
    return render(request, "app/trailer.html", context)

def not_available(request):
    return render(request,'app/not_available.html')

def register_page(request):
    form = CustomUserForm()

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Signed In Now You Can Sign Up")
    return render(request,'app/register.html',{'form':form})

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Signed Up Welcome to HrzFlix !")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username and Password")

    return render(request,'app/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Signed Out")
    return redirect("/")

def addtolater(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            movie_id = data['movieId']
            movie_status = Movie.objects.get(id=movie_id)

            if movie_status:
                if WatchLater.objects.filter(user=request.user.id,movies_id=movie_id):
                    return JsonResponse({'status':'Already Added to Watch Later'})
                else:
                    WatchLater.objects.create(user=request.user,movies_id=movie_id)
                    return JsonResponse({'status':'Added to Watch Later'},status=200)
            else:
                return JsonResponse({'status':'Invalid Movie ID'})

        else:
            return JsonResponse({'status':'Login to Add To Watch Later'})
                    
    else:
        return JsonResponse({'status':'Invalid Access'},staus=400)  
    
def watchlater_page(request):
    if request.user.is_authenticated:
        watchlater = WatchLater.objects.filter(user=request.user)
        return render(request,'app/watchlater.html',{'watchlater':watchlater})
    else:
        return redirect('login')
    
def removelater(request,mid):
    lateritems = WatchLater.objects.get(id=mid)
    lateritems.delete()
    return redirect('/watchlater')


    
    