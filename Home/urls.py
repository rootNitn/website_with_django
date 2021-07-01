from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='about'),
    path("videos", views.videos, name='videos'),
    path("contact", views.contact, name='contact'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),
    path("player", views.player, name='player'),
   
    path("logout", views.logouthandle, name='logouthandle'),
]