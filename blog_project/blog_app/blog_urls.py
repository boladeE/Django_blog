from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("new_post", views.new_post, name='new_post_page'),
    path("user_post/<int:pk>", views.reading_posts, name='reading_post_page'),
    path("update_user_post/<int:pk>", views.updating_posts, name='updating_post_page'),
    path("delete_post/<int:pk>", views.deleting_posts, name='delete_post_page')
]
