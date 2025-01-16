from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
  path('devtools', devtools, name='devtools'),
  path('devtools_create', devtools_create, name='devtools_create'),
  path('devtools_detail/<int:pk>', devtools_detail, name='devtools_detail'),
  path('devtools_update/<int:pk>', devtools_update, name='devtools_update'),
  path('devtools_delete/<int:pk>', devtools_delete, name='devtools_delete'),
  path('<int:pk>', devtools_detail, name='devtools_detail'),
]