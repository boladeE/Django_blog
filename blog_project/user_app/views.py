from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from transformers import pipeline

# Load the model and tokenizer from Hugging Face
generator = pipeline('text-generation', model='gpt2')

def generate_blog_post(prompt):
    from transformers import pipeline
    generator = pipeline('text-generation', model='gpt2')
    response = generator(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']


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