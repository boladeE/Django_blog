from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'user_app/sign_up.html', {'sign_up_form': form})

@login_required
def profile(request):
    return render(request, 'user_app/profiles.html')