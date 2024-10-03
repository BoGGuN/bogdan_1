from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет Джанго 3')

def old_link(response):
    return HttpResponse('Новая новая ссылка 3')

def oldest_link(response):
    return HttpResponse('OLD_LINKER OLD TOWN ROAD раньше было лучше')