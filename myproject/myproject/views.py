# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World!\nWelcome to Django")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This page will display the about page")
    return render(request, 'about.html')