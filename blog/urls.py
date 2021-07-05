from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    
    path("profile", views.profile, name='profile'),
    path("newblog", views.newblog, name='newblog'),
    path("allblog", views.allblog, name='allblog'),
    path("<str:slug>", views.blogspost, name='blogspost'),
]