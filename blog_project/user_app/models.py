from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        default="default_img.jpeg", upload_to="profile_pictures"
    )

    def __str__(self):
        return f"{self.user.username} Profile"
