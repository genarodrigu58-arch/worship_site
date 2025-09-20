from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    key = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que publicó
    content = models.TextField()  # El mensaje
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de publicación

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    instrument = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
