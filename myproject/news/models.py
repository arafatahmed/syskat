from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=50)
    short_txt = models.CharField(max_length=50)
    body_txt = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    pic = models.CharField(default='0', max_length=50)
    writer = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name