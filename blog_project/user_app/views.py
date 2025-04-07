from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm, SignUpForm, UserUpdateForm


class PasswordsChangeView(PasswordChangeView, SuccessMessageMixin):
    template_name = "user_app/change_password.html"
    success_url = "/"
    success_message = "Your password has been successfully changed"


class LoginView(LoginView, SuccessMessageMixin):
    template_name = "user_app/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Login successful! Welcome back.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


class LogoutView(LogoutView, SuccessMessageMixin):
    next_page = "/"
    # success_message = 'You have successfully logged out'

    # def dispatch(self, request, *args, **kwargs):
    #     messages.info(request, "You have been logged out successfully.")
    #     return redirect("login_page")  # Redirect to login page


class PasswordResetView(PasswordResetView, SuccessMessageMixin):
    template_name = "user_app/reset_password.html"


class PasswordResetDoneView(PasswordResetDoneView, SuccessMessageMixin):
    template_name = "user_app/password_reset_sent.html"


class PasswordResetConfirmView(PasswordResetConfirmView, SuccessMessageMixin):
    template_name = "user_app/password_reset_form.html"


class PasswordResetCompleteView(PasswordResetCompleteView, SuccessMessageMixin):
    template_name = "user_app/password_reset_done.html"


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Account has successfully been created")
            return redirect("login_page")
    else:
        form = SignUpForm()
    return render(request, "user_app/sign_up.html", {"sign_up_form": form})


@login_required
def update_profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST, instance=request.user
        )  # Bind form to the existing post instance
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile has successfully been updated")

    else:
        u_form = UserUpdateForm(
            instance=request.user
        )  # Bind form to the existing post instance
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "user_app/update_profile.html", context)


@login_required
def profile(request):
    return render(request, "user_app/profiles.html")
