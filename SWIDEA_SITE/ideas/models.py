from django.db import models
from devtools.models import Devtool

class Idea(models.Model):
  title = models.CharField('아이디어명', max_length=50)
  image = models.ImageField('Image', upload_to='ideas/%Y%m%d', blank=True)
  content = models.TextField('아이디어 설명')
  interest = models.IntegerField('아이디어 관심도', default=0)
  devtool = models.ForeignKey(Devtool, null=True, on_delete=models.CASCADE, verbose_name='예상 개발툴')
  IdeaStar = models.BooleanField('찜하기', default=False)