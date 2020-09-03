from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.TextField()
    genre = models.TextField(default='')
    rating = models.TextField(default='')
    tanggal = models.TextField(default='')
    deskripsi = models.TextField(default='')

class Game(models.Model):
    judul = models.TextField()
    deskripsi = models.TextField(default='')
