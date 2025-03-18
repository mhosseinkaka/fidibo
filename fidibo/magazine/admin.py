from django.contrib.admin import ModelAdmin, register
from magazine.models import Magazine_detail

# Register your models here.
@register(Magazine_detail)
class Magazine_detailAdmin(ModelAdmin):
    list_display = ['title', 'name', 'mag_number', 'price', 'print_time']
    search_fields = ['title', 'name', 'price']
    autocomplete_fields = ['book_buy']
    