from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.

class option(models.Model):
    theme = models.CharField(max_length=200, primary_key=True)
    option1_text = models.CharField(max_length=200)
    option2_text = models.CharField(max_length=200)
    def __str__(self):
        return self.theme
