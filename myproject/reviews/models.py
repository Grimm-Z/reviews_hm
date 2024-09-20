from django.db import models
from datetime import datetime

# Create your models here.
class review(models.Model):
    user = models.CharField(max_length=25)
    text = models.TextField(default='Some text')
    date = models.DateTimeField(default=datetime.now())