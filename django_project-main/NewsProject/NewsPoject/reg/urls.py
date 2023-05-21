from django.contrib import admin
from django.urls import path, include

from reg.views import register, login

urlpatterns = [
    path('register', register, name='Register'),
    path('login', login, name='Login'),
]