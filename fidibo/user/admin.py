from django.contrib.admin import ModelAdmin, register
from user.models import Customer

# Register your models here.
@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    