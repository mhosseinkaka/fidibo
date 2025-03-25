from django.http.response import HttpResponse, JsonResponse
import os
from user.models import Book
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Book.objects.create(
            name = data.get('name'),
            book_number = data.get('book_number'),
            author = data.get('author'),
            price = data.get('price'),
            print_time = data.get('print_time')
        )
    return HttpResponse("OK!!!")