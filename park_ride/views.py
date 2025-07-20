from django.http import HttpResponse  # if you want to use HttpResponse (optional)
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'home.html')  # or 'park_ride/home.html' if it's in subfolder
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or your home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'