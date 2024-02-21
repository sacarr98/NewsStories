from django.shortcuts import render
from django.http import HttpResponse

def your_news(request):
    return HttpResponse("Hello, World")