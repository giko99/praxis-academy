from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.TextField()
    genre = models.TextField(default='')
    deskripsi = models.TextField(default='')
