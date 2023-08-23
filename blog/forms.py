from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Post


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "email", "password1", "password2"]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description")
