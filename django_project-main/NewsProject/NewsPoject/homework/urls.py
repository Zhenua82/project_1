from django.contrib import admin
from django.urls import path

from homework.views import home, get_profession, human_1

urlpatterns = [
    path('home/', home, name='Home'),
    path('profession/<int:profession_id>', get_profession, name='Profession'),
    path('home/<int:human_id>', human_1, name='human_1')
]