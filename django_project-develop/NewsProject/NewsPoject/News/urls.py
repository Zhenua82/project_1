from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from News.views import index

urlpatterns = [
    path('', index),
    path('homework/', include('homework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
