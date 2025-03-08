from django.urls import path
from .views import v_book

urlpatterns = [
    path('v-book', v_book)
]