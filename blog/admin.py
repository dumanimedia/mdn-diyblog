from django.contrib import admin

from .models import Blogger, Comment, Post

admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Comment)
