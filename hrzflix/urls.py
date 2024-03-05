from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path("movies",views.movies,name="movies"),
    path("animes",views.animes,name="animes"),
    path("series",views.series,name="series"),
    path("movies/<str:name>/",views.movie_details,name="movies"),
    path("animes/<str:name>/",views.movie_details,name="animes"),
    path("series/<str:name>/",views.movie_details,name="series"),
    path('movies/<str:name>/trailer', views.trailer_view, name='trailer_view'),
    path('<str:name>/trailer', views.trailer_view_2, name='trailer_view_2'),
    path('not_available', views.not_available, name='not_available'),
    path("register",views.register_page,name="register"),
    path("login",views.login_page,name="login"),
    path("logout",views.logout_page,name="logout"),
    path("addToLater",views.addtolater,name="addToLater"),
    path("watchlater",views.watchlater_page,name="watchlater"),
    path("removelater/<str:mid>",views.removelater,name="removelater"),
]