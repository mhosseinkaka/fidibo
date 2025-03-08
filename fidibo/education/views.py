from django.http.response import HttpResponse

def education_college(response):
    return HttpResponse(" کتب درسی دانشگاهی")

def education_highschool(response):
    return HttpResponse("کتب درسی دبیرستان")

def education_school(response):
    return HttpResponse("کتب درسی دبستان")
