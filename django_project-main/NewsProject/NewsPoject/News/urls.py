from django.contrib import admin
from django.urls import path, include


from News.views import index

urlpatterns = [
    path('', index),
    path('homework/', include('homework.urls')),
]
