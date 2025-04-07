from django import forms

from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post  # Link the form to the BlogPost model
        fields = ["title", "content"]
