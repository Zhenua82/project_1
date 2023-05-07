from django.shortcuts import render
from .models import Human, Profession

def home(request):
    human = Human.objects.all()
    professions = Profession.objects.all()
    context = {
        'human': human,
        'title': 'Список людей',
        'title2': 'Список людей:',
        'professions': professions
    }
    return render(request, 'homework/home.html', context=context)

def get_profession(request, profession_id):
    human = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'human': human,
        'professions': professions,
        'profession': profession
    }
    return render(request, 'homework/profession.html', context=context)