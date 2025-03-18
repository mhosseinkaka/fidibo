from django.db import models
from user.models import Customer

class Book(models.Model):
    name = models.CharField(max_length=100)
    book_number = models.CharField(max_length=15)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    print_time = models.DateTimeField()
    book_buy = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="e_book", blank=True, null=True)

    
