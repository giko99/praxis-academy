from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

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

def tabelmerch(req):
    merch = models.Merch.objects.all()
    return render(req, 'merch/daftarmerch.html', {
        'data': merch,
    })

def input(req):
    form_input = forms.TaskForm()

    if req.POST:
        form_input = forms.TaskForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/daftarfilm')
    
    task = models.Task.objects.all()    
    return render(req, 'task/input.html', {
        'data': task,
        'form': form_input,
    })

def input_g(req):
    form_input = forms.GameForm()

    if req.POST:
        form_input = forms.GameForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/game/daftargame')

    game = models.Game.objects.all()    
    return render(req, 'game/input.html', {
        'data': game,
        'form': form_input,
    })

def input_m(req):
    form_input = forms.MerchForm()

    if req.POST:
        form_input = forms.MerchForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/merch/daftarmerch')

    merch = models.Merch.objects.all()    
    return render(req, 'merch/input.html', {
        'data': merch,
        'form': form_input,
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

def detail_m(req, id):
    merch = models.Merch.objects.filter(pk=id).first()    
    return render(req, 'merch/detail.html', {
        'data': merch,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/daftarfilm')

def delete_g(req, id):
    models.Game.objects.filter(pk=id).delete()
    return redirect('/game/daftargame')

def delete_m(req, id):
    models.Merch.objects.filter(pk=id).delete()
    return redirect('/merch/daftarmerch')

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

def update_m(req, id):
    if req.POST:
        merch = models.Merch.objects.filter(pk=id).update(nama=req.POST['nama'], kategori=req.POST['kategori'], harga=req.POST['harga'], stock=req.POST['stock'], deskripsi=req.POST['deskripsi'])
        return redirect('/merch/daftarmerch')

    merch = models.Merch.objects.filter(pk=id).first()    
    return render(req, 'merch/update.html', {
        'data': merch,
    })

