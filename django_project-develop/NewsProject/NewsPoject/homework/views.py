from django.shortcuts import render
from .models import Human

def home(ddd):
    human = Human.objects.all()
    context = {
        'human': human,
        'title': 'Список людей',
        'title2': 'Список людей:'
    }
    return render(ddd, 'homework\home.html', context=context)
