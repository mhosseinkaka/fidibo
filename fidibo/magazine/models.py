from django.db import models
from user.models import Customer

class Magazine_detail(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    mag_number = models.CharField(max_length=15)
    author_1 = models.CharField(max_length=100)
    author_2 = models.CharField(max_length=100)
    author_3 = models.CharField(max_length=100)
    author_4 = models.CharField(max_length=100)
    price = models.IntegerField()
    print_time = models.DateTimeField()
    book_buy = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="magazine", blank=True, null=True)
