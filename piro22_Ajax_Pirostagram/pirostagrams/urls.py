from django.urls import path
from .views import *

app_name = 'pirostagrams'

urlpatterns = [
    path('', pirostagram, name='pirostagram'),
    path('post_new/', post_new, name='post_new'),
    path('post/<int:pk>', post, name='post'),
    path('like_ajax/', like_ajax, name='like_ajax'),
]