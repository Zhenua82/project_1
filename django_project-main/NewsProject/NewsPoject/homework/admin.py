from django.contrib import admin
from .models import Human, Profession


class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Last_name', 'age', 'biography', 'profession', 'photo', 'is_published')
    list_display_links = ('id', 'Name')
    search_fields = ('Name', 'Last_name')
    list_editable = ['is_published', 'profession']

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

