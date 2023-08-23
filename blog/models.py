from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    DateTimeField,
    TextField,
)


class Blogger(Model):
    user = ForeignKey(to=User, on_delete=CASCADE)
    bio = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-created_at"]


class Post(Model):
    title = CharField(max_length=250)
    description = TextField()
    blogger = ForeignKey(to=Blogger, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(Model):
    post = ForeignKey(to=Post, on_delete=CASCADE)
    user = ForeignKey(to=User, on_delete=CASCADE)
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'By {self.user.username} on post "{self.post.title}"'
