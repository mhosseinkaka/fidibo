from django.db import models
from e_book.models import Book
from magazine.models import Magazine_detail
from v_book.models import V_book
from education.models import Eduaction_book

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True)
    book_buy = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="e_book")
    book_buy = models.ForeignKey(to=Magazine_detail, on_delete=models.CASCADE, related_name="magazine")
    book_buy = models.ForeignKey(to=V_book, on_delete=models.CASCADE, related_name="v_book")
    book_buy = models.ForeignKey(to=Eduaction_book, on_delete=models.CASCADE, related_name="education_book")