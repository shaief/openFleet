from registration.forms import RegistrationForm
from django import forms


class RegistrationForm(RegistrationForm):
    username = forms.CharField(label="User name:")
    username = forms.EmailField(label="Email address:")
    first_name = forms.CharField(label="First name:")
    last_name = forms.CharField(label="Last name:")
    is_human = forms.ChoiceField(label="Are you human?:")
