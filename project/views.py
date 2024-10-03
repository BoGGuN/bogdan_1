from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет Джанго')

def catalog(response):
    return HttpResponse('Каталог')

def wowa(response):
    return HttpResponse('WOWA!!!!!!!!!!!')