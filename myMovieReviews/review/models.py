from django.db import models

class Review(models.Model):
  title = models.TextField()
  year = models.TextField()
  jenre = models.TextField()
  starrating = models.TextField()
  runningtime = models.IntegerField()
  content = models.TextField()
  director = models.TextField()
  actor = models.TextField()

  def formatted_runningtime(self):
    hours = self.runningtime // 60
    minutes = self.runningtime % 60
    return f"{hours}시간 {minutes}분" if hours > 0 else f"{minutes}분"