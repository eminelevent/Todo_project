from django.db import models
from datetime import datetime

class todos(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length=100, blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.title