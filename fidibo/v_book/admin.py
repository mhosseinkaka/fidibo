from django.contrib.admin import ModelAdmin, register
from v_book.models import V_book
# Register your models here.
@register(V_book)
class V_bookAdmin(ModelAdmin):
    list_display = ['name', 'author', 'price']
    list_filter = ['name', 'author', 'price']
    autocomplete_fields = ['book_buy']