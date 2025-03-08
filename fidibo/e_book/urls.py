from django.urls import path
from .views import e_book

urlpatterns = [
    path('e-book', e_book)
]