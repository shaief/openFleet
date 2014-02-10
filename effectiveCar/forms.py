from django import forms
from django.core.exceptions import ValidationError

from effectiveCar.models import Car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car

    