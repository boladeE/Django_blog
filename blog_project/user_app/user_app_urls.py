from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(template_name="user_app/login.html"), name='login_page'),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/"), name='logout_page'),
    path("sign_up", views.sign_up, name='sign_up_page'),
    path("sign_in", views.sign_in, name='sign_in_page'),
    path("log_out", views.log_out, name='log_out_page')
]