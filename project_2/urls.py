from django.urls import path
from project_2.views import index, new_link, porch

urlpatterns = [
    path('', index),
    path('new_link/', new_link),
    path('porch911/',porch)
]