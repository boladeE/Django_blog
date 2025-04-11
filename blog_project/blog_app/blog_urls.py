from django.urls import path

from . import views

# Function based url patterns
# urlpatterns = [
#     path("", views.home_page, name='home_page'),
#     path("new_post", views.new_post, name='new_post_page'),
#     path("user_post/<int:pk>", views.reading_posts, name='reading_post_page'),
#     path("update_user_post/<int:pk>", views.updating_posts, name='updating_post_page'),
#     path("delete_post/<int:pk>", views.deleting_posts, name='delete_post_page')
# 

# Class based url patterns
urlpatterns = [
    path("", views.PostListView.as_view(), name="home_page"),
    path("about", views.about_page, name="about_page"),
    path("new_post", views.PostCreateView.as_view(), name="new_post_page"),
    path(
        "user_post/<int:pk>", views.PostDetailView.as_view(), name="reading_post_page"
    ),
    path(
        "update_user_post/<int:pk>",
        views.PostUpdateView.as_view(),
        name="updating_post_page",
    ),
    path(
        "delete_post/<int:pk>", views.PostDeleteView.as_view(), name="delete_post_page"
    ),
]
