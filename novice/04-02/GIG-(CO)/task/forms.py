from django.forms import ModelForm

from . import models 

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        exclude = []

class GameForm(ModelForm):
    class Meta:
        model = models.Game
        exclude = []

class MerchForm(ModelForm):
    class Meta:
        model = models.Merch
        exclude = []