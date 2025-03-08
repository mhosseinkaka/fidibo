from django.http.response import HttpResponse

def mag_family(response):
    return HttpResponse("مجله خانواده")

def mag_child(response):
    return HttpResponse("مجله کودک")

def mag_cook(response):
    return HttpResponse("مجله آشپزی")

