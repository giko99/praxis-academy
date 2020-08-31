from django.shortcuts import render

# Create your views here.
from . import models

def index(req):
    if req.POST:
        models.film.objects.create(judul=req.POST['judul'], genre=req.POST['genre'], rating=req.POST['rating'], tanggal=req.POST['tanggal'], deskripsi=req.POST['deskripsi'])

    films = models.film.objects.all()
    return render (req, 'list/index.html', {
        'data' : films,
    })