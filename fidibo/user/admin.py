from django.contrib.admin import ModelAdmin, register
from user.models import Customer, Book

# Register your models here.
@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('name', 'book_number', 'author', 'price', 'print_time')
    search_fields = ('name', 'book_number', 'author', 'price')
    