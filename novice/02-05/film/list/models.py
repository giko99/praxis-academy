from django.db import models

# Create your models here.
class film(models.Model):
    judul  = models.TextField()
    genre = models.TextField(default='')
    rating = models.TextField(default='')
    tanggal  = models.TextField(default='')
    deskripsi = models.TextField(default='')
