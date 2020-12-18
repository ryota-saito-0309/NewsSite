from django.db import models
from django.urls import reverse

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=4000, null=True, blank=True, default='a')
    date = models.DateField()
    url = models.URLField(null=True, blank=True, default="")


