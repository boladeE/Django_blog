from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("input", views.user_input)
]
