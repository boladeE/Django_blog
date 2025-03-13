from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Account has successfully been created")
            return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'user_app/sign_up.html', {'sign_up_form': form})

@login_required
def update_profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # Bind form to the existing post instance
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile has successfully been updated")

    else:
        u_form = UserUpdateForm(instance=request.user)  # Bind form to the existing post instance
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_app/update_profile.html', context)

@login_required
def profile(request):
    return render(request, 'user_app/profiles.html')