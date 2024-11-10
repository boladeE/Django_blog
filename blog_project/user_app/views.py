from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import signUp

def sign_up(request):
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in_page')
    else:
        form = signUp()
    return render(request, 'user_app/sign_up.html', {'sign_up': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'{username}, {password}')
        user = authenticate(username = username, password = password)

        if user is not None:
            return redirect('home_page')
        
    else:
        form
        return render(request, 'user_app/sign_in.html', {'sign_in': form})
    return render (request, 'user_app/sign_in.html')
