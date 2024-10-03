from django.urls import path
from project.views import index, catalog, wowa

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('wowa/', wowa)
]