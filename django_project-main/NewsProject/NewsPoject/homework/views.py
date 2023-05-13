from django.shortcuts import render, get_object_or_404, redirect
from .models import Human, Profession
from .forms import HumanForm

def home(request):
    human = Human.objects.all()
    professions = Profession.objects.all()
    context = {
        'human': human,
        'title': 'Список людей',
        'title2': 'Список людей:',

    }
    return render(request, 'homework/home.html', context=context)

def get_profession(request, profession_id):
    human = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'human': human,
        'profession': profession
    }
    return render(request, 'homework/profession.html', context=context)

def human_1(request, human_id):
    # human_i = Human.objects.get(pk=human_id)
    human_i = get_object_or_404(Human, pk=human_id)
    context = {
        'human_i': human_i
    }
    return render(request, 'homework/human_1.html', context=context)

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            # human = Human.objects.create(**form.cleaned_data)
            human = form.save()
            return redirect(human)
    else:
        form = HumanForm()
    return render(request, 'homework/add_human.html', {'form': form})