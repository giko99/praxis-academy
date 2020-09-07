from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    tanggal = models.CharField(max_length=255)
    deskripsi = models.TextField(default='')
