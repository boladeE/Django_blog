from django.urls import path
from . import views

urlpatterns = [
    path("sign_up", views.sign_up, name='sign_up_page'),
    path("sign_in", views.sign_in, name='sign_in_page'),
    path("log_out", views.log_out, name='log_out_page')
]
