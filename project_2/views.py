from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет Джанго 2')

def new_link(response):
    return HttpResponse('Новая новая ссылка 2')

def porch(response):
    return HttpResponse('PORHC')