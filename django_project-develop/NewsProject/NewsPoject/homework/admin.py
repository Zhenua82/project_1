from django.contrib import admin
from .models import Human

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Last_name', 'age', 'profession', 'photo', 'is_published')
    list_display_links = ('id', 'Name')
    search_fields = ('Name', 'Last_name')


admin.site.register(Human, HumanAdmin)


