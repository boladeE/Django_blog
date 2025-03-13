from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(template_name="user_app/login.html"), name='login_page'),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/"), name='logout_page'),
    path("sign_up", views.sign_up, name='sign_up_page'),
    path("profile", views.profile, name='profile_page'),
    path("update_profile", views.update_profile, name='update_profile_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
