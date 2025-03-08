from django.urls import path
from .views import mag_child, mag_cook, mag_family

urlpatterns = [
    path('mag-family', mag_family),
    path('mag-child', mag_child),
    path('mag-cook', mag_cook)
]