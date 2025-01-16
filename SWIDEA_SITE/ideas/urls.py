from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
  path('', main, name='main'),
  path('ideas_create', ideas_create, name='ideas_create'),
  path('ideas_detail/<int:pk>', ideas_detail, name='ideas_detail'),
  path('ideas_delete/<int:pk>', ideas_delete, name='ideas_delete'),
  path('ideas_update/<int:pk>', ideas_update, name='ideas_update'),
  path('<int:pk>/IdeaStar', IdeaStarToggle, name='ideas_IdeaStarToggle'),
]