from django.contrib.admin import ModelAdmin, register
from education.models import Eduaction_book
# Register your models here.

@register(Eduaction_book)
class Eduaction_bookAdmin(ModelAdmin):
    search_fields = ['name', 'author', 'level']
    list_display = ['name', 'author', 'level']
    autocomplete_fields = ['book_buy']
    