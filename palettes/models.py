from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Table for storing palettes info
class Palettes(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)