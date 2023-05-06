from . import views
from django.contrib import admin
from django.urls import path

from .views import home_view, base_view, programs_view, addprograms_view, register_user, login_view, logout_view, signup_view


urlpatterns = [
    path('base/', base_view, name='base'),
    path('home/', home_view, name='home'),
    path('programs/', programs_view, name='programs'),
    path('addprograms/', addprograms_view, name='addprograms'),
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup')
]
