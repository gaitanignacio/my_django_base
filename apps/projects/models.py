from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default = '', blank=True, null=True)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=datetime.now())
