from django.db import models


class V_book(models.Model):
    name = models.CharField(max_length=100)
    book_number = models.CharField(max_length=15)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    print_time = models.DateTimeField()
    field = models.CharField(max_length=50)
    time = models.TimeField()
