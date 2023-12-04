from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home (request):
    return HttpResponse ("Hello Welcome to Home page")

def section1 (request):
    return HttpResponse ("Welcome to Section 1")

def hello(request):
    return HttpResponse("HI")