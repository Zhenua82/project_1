from django.shortcuts import render, get_object_or_404
from .models import News, Category

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'News/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'News/category.html', context=context)

def view_news(request, news_id):
    # news_i = News.objects.get(pk=news_id)
    news_i = get_object_or_404(News, pk=news_id)
    context = {
        'news_i': news_i
    }
    return render(request, 'News/view_news.html', context=context)

