from django.contrib import admin
from django.urls import path, include


from News.views import HomeNews, NewsByCategory, AddNews, ViewNews, test, register, login
# from News.views import index, get_category, view_news, add_news, test
urlpatterns = [
    # path('', index, name='News'),
    # path('category/<int:category_id>/', get_category, name='Category'),
    # path('news/add_news', add_news, name='Add_news'),
    # path('news/<int:news_id>/', view_news, name='View_news'),
    path('test/', test, name='Test'),
    path('', HomeNews.as_view(), name='News'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('register', register, name='Register'),
    path('login', login, name='Login'),

    path('homework/', include('homework.urls')),
]
