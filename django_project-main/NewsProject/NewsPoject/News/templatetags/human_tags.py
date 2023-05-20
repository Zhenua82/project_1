from homework.models import Profession
from django import template
from django.db.models import Count, F

register = template.Library()
@register.simple_tag(name='get_list_profession')
def get_profession():
    # return Profession.objects.all()
    return Profession.objects.annotate(cnt=Count('human'))

@register.inclusion_tag('homework/list_profession.html')
def show_professions(arg1='Перечень', arg2='профессий'):
    # professions = Profession.objects.all()
    # professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
    professions = Profession.objects.annotate(cnt=Count('human', filter=F('human__is_published'))).filter(cnt__gt=0)
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}
