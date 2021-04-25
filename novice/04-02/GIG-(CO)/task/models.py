from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    genre_choice = [
        ("Drama", "Drama"),
        ("Romance", "Romance"),
        ("Action", "Action"),
        ("Thriler", "Thriler"),
        ("Mistery", "Mistery"),
        ("Fiction", "Fiction"),
    ]
    genre = MultiSelectField(max_length=25, choices = genre_choice, default='1')
    rating = models.CharField(max_length=255)
    tanggal = models.CharField(max_length=255)
    upload_img = models.ImageField(default='', upload_to="images/")
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