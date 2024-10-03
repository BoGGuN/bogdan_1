from django.urls import path
from python_3.views import index, old_link, oldest_link

urlpatterns = [
    path('', index),
    path('old_link/', old_link),
    path('oldest_link/', oldest_link)
]