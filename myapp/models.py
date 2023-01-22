from django.db import models

class Chuvas(models.Model):
  data = models.CharField(max_length=20)
  volume = models.IntegerField()