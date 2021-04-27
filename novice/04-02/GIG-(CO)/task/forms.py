from django.forms import ModelForm
from django import forms
from datetime import datetime, date
from bootstrap_datepicker_plus import DatePickerInput
from . import models

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        exclude = []
        widgets = {
            'tanggal': DatePickerInput(format='%d-%m-%Y').start_of('event days'),
        }

class GameForm(ModelForm):
    class Meta:
        model = models.Game
        exclude = []

class MerchForm(ModelForm):
    class Meta:
        model = models.Merch
        exclude = []