from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts',null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.user.username} on {self.publication_date}"



class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post.id}"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date_followed = models.DateTimeField(auto_now_add=True)