from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello World!\nWelcome to Django")


def about(request):
    return HttpResponse("This page will display the about page")