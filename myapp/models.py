from django.db import models
from datetime import datetime

# Create your models here.
class news(models.Model):
    title=models.CharField(max_length=100)
    details= models.CharField(max_length=2000)
    user = models.CharField(max_length=30)