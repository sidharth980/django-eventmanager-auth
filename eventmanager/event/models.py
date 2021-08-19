from django.db import models


class Event(models.Model):
    eventName = models.CharField(max_length=100)
    createdDate = models.DateField()
    eventTime = models.DateField() 
    about = models.TextField()
    author = models.CharField(max_length=50)