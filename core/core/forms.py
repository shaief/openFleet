from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
