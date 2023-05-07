from django.contrib import admin
from django.urls import path, include


from News.views import index, get_category

urlpatterns = [
    path('', index, name='News'),
    path('homework/', include('homework.urls')),
    path('category/<int:category_id>', get_category, name='Category')
]
