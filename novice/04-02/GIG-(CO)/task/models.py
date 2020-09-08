from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    tanggal = models.CharField(max_length=255)
    deskripsi = models.TextField(default='')

class Game(models.Model):
    judul = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    tanggal = models.CharField(max_length=255)
    deskripsi = models.TextField(default='')

class Merch(models.Model):
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    deskripsi = models.TextField(default='')