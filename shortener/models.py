from django.conf.urls import url
from django.db import models

# Create your models here.
class URLData(models.Model):
    url = models.CharField(max_length=250)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return "URL: {self.url} Short-URL: {self.slug}"
