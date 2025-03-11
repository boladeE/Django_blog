from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in_page')
    else:
        form = SignUpForm()
    return render(request, 'user_app/sign_up.html', {'sign_up_form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user=user)
            return redirect('home_page')

    else:
        form = AuthenticationForm()
    return render (request, 'user_app/sign_in.html', {'sign_in_form': form})


def log_out(request):
    logout(request)
    return redirect('sign_in_page')

def profile(request):
    return render(request, 'profiles.html')