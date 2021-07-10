from django.contrib import admin, auth
from django.urls import path
from Home import views as ho
from django.contrib.auth import views as auth_views
from blog import views as bb

urlpatterns = [
    path("", ho.index, name='Home'),
    path("about", ho.about, name='about'),
    path("videos", ho.videos, name='videos'),
    path("contact", ho.contact, name='contact'),
    path("signin", ho.signin, name='signin'),
    path("signup", ho.signup, name='signup'),
    path("player", ho.player, name='player'),
    path("chatbot", ho.chatbot, name='chatbot'),
    #path("blogs", bb.blogs, name='blog'),
    #path("profile", bb.profile, name='profile'),
    #path("newblog", bb.newblog, name='newblog'),
    path("logout", ho.logouthandle, name='logouthandle'),
    
    # reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("<str:idi>", ho.player, name='player'),

]