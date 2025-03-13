from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("reading_post_page", kwargs={"pk": self.pk})
# Create your models here.
