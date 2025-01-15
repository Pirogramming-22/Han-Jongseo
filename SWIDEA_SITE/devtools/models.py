from django.db import models

class Devtool(models.Model):
  name = models.CharField('이름', max_length=50)
  kind = models.CharField('종류', max_length=50)
  content = models.TextField('개발툴 설명')