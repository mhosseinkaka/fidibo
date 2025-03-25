from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    book_number = models.CharField(max_length=15)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    print_time = models.DateTimeField()

