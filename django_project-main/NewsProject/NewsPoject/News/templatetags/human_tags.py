from homework.models import Profession
from django import template

register = template.Library()
@register.simple_tag(name='get_list_profession')
def get_profession():
    return Profession.objects.all()

@register.inclusion_tag('homework/list_profession.html')
def show_professions(arg1='Перечень', arg2='профессий'):
    professions = Profession.objects.all()
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}
