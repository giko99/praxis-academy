from django.shortcuts import render, redirect

# Create your views here.
from . import models

def index(req):
    task = models.Task.objects.all()
    game = models.Game.objects.all()
    return render(req, 'task/index.html', {
        'data': task, 
    })

def tabelfilm(req):
    task = models.Task.objects.all()
    return render(req, 'task/daftarfilm.html', {
        'data': task,
    })

def tabelgame(req):
    game = models.Game.objects.all()
    return render(req, 'game/daftargame.html', {
        'data': game,
    })

def input(req):
    if req.POST:
        task = models.Task.objects.create(name=req.POST['name'], genre=req.POST['genre'], rating=req.POST['rating'], tanggal=req.POST['tanggal'], deskripsi=req.POST['deskripsi'])
        return redirect('/daftarfilm')
    
    task = models.Task.objects.all()    
    return render(req, 'task/input.html', {
        'data': task,
    })

def input_g(req):
    if req.POST:
        game = models.Game.objects.create(judul=req.POST['judul'], deskripsi=req.POST['deskripsi'])
        return redirect('/game/daftargame')
    
    game = models.Game.objects.all()    
    return render(req, 'game/input.html', {
        'data': game,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()    
    return render(req, 'task/detail.html', {
        'data': task,
    })

def detail_g(req, id):
    game = models.Game.objects.filter(pk=id).first()    
    return render(req, 'game/detail.html', {
        'data': game,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/daftarfilm')

def delete_g(req, id):
    models.Game.objects.filter(pk=id).delete()
    return redirect('/game/daftargame')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(name=req.POST['name'], genre=req.POST['genre'], rating=req.POST['rating'], tanggal=req.POST['tanggal'], deskripsi=req.POST['deskripsi'])
        return redirect('/daftarfilm')

    task = models.Task.objects.filter(pk=id).first()    
    return render(req, 'task/update.html', {
        'data': task,
    })

def update_g(req, id):
    if req.POST:
        game = models.Game.objects.filter(pk=id).update(judul=req.POST['judul'], deskripsi=req.POST['deskripsi'])
        return redirect('/game/daftargame')

    game = models.Game.objects.filter(pk=id).first()    
    return render(req, 'game/update.html', {
        'data': game,
    })
