from django.contrib.admin import ModelAdmin, register
from e_book.models import Book

# Register your models here.
@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ['name', 'author', 'price']
    search_fields = ['name', 'author']
    autocomplete_fields = ['book_buy']