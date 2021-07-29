from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(requst):
    return HttpResponse("Rango says hey there partner")