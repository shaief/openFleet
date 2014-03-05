from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

from effectiveCar.models import Car, Owner, Classification



class CarForm(forms.ModelForm):
    class Meta:
        model = Car

    def __init__(self, *args, **kwargs):
        date_of_purchase = forms.DateField(widget=SelectDateWidget)

