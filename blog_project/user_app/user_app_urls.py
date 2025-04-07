from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("sign_up", views.sign_up, name="sign_up_page"),
    path("profile", views.profile, name="profile_page"),
    path("accounts/login/", views.LoginView.as_view(), name="login_page"),
    path("accounts/logout/", views.LogoutView.as_view(), name="logout_page"),
    path("update_profile", views.update_profile, name="update_profile_page"),
    path("reset_password/", views.PasswordResetView.as_view(), name="reset_password"),
    path(
        "reset_password_sent/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/change_password",
        views.PasswordsChangeView.as_view(),
        name="change_password_page",
    ),
    path(
        "reset/<uidb64>/<token>",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
