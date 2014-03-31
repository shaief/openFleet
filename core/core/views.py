from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

from .forms import RegistrationForm

User = get_user_model()


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
