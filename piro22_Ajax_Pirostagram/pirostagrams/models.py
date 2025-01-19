from django.db import models

class Post(models.Model):
  content = models.TextField(default="내용을 입력하세요")
  like = models.IntegerField(default=0)