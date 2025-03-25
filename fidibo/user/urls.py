from django.urls import path
from user.views import add_book

urlpatterns = [
    path('add-book/', add_book)
]