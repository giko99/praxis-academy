from django.shortcuts import render

from . import models

# Create your views here.
def index(req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'], status=req.POST['status'])
    
    tasks = models.Task.objects.all()
    return render(req, 'task/index.html',{
        'data' :tasks,
    })