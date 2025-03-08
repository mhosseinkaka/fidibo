from django.urls import path
from .views import education_college, education_highschool,education_school

urlpatterns = [
    path('college', education_college),
    path('high-school', education_highschool),
    path('school', education_school)
]