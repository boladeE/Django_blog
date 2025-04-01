import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='pass123')

@pytest.fixture
def post(user):
    return Post.objects.create(title='Test Post', content='Test content', user=user)

@pytest.mark.django_db
def test_post_creation(user, post):
    assert post.title == 'Test Post'
    assert post.content == 'Test content'
    assert post.user.username == 'testuser'

@pytest.mark.django_db
def test_get_absolute_url(post):
    url = reverse("reading_post_page", kwargs={"pk": post.pk})
    assert post.get_absolute_url() == url

@pytest.mark.django_db
def test_post_list_view(client, post):
    response = client.get(reverse('home_page'))
    assert response.status_code == 200
    assert post.title in response.content.decode()

@pytest.mark.django_db
def test_post_detail_view(client, post):
    response = client.get(reverse('reading_post_page', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert post.title in response.content.decode()
