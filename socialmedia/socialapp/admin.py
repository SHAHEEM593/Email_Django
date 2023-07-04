from django.contrib import admin
from .models import User, Profile, Post, Like, Comment, Tag, Follow

admin.site.register(User)

admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(Like)

admin.site.register(Comment)

admin.site.register(Tag)

admin.site.register(Follow)

