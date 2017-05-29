from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

class image(models.Model):
#    camera = models.IntegerField()
    imagelink = models.URLField(max_length=200)
    def __str__(self):
        return self.imagelink
