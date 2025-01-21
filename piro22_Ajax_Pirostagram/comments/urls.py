from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('comment/<int:pk>/create', comment_create, name='comment_create'),
    path('comment/<int:pk>', comment_delete, name='comment_delete'),
]