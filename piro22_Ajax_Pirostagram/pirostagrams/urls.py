from django.urls import path
from .views import *

app_name = 'pirostagrams'

urlpatterns = [
    path('', pirostagram, name='pirostagram'),
]