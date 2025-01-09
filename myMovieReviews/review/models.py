from django.db import models

class Review(models.Model):
  title = models.TextField()
  year = models.TextField()
  jenre = models.TextField()
  starrating = models.TextField()
  runningtime = models.TextField()
  content = models.TextField()
  director = models.TextField()
  actor = models.TextField()