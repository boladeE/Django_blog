import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_signup(client):
    signup_url = reverse('sign_up_page')
    response = client.post(signup_url, {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'Testpassword123',
        'password2': 'Testpassword123'
    })
    # Expect redirect after signup
    assert response.status_code == 302
    assert User.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_login(client):
    User.objects.create_user(username='testuser', password='pass123')
    login_url = reverse('login_page')
    response = client.post(login_url, {
        'username': 'testuser',
        'password': 'pass123'
    })
    assert response.status_code == 302

@pytest.mark.django_db
def test_profile_view_authenticated(client):
    user = User.objects.create_user(username='testuser', password='pass123')
    client.login(username='testuser', password='pass123')
    profile_url = reverse('profile_page')
    response = client.get(profile_url)
    assert response.status_code == 200
    assert user.username in response.content.decode()
