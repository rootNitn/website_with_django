from django.contrib import admin, auth
from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='about'),
    path("videos", views.videos, name='videos'),
    path("contact", views.contact, name='contact'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),
    path("player", views.player, name='player'),
   
    path("logout", views.logouthandle, name='logouthandle'),
    # reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]