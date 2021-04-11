from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    publicher = models.ForeignKey(
        User, related_name="Posts", on_delete=models.CASCADE)
    body = models.TextField(max_length=900)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True)


class Like(models.Model):
    pass
    # post = models.ForeignKey(Post, related_name="likeea",
    #                          on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name="likes",
    #                          on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments",
                             on_delete=models.CASCADE)
    Comment = models.CharField(max_length=400)


class FollowUp(models.Model):
    follower = models.ForeignKey(User, related_name="followers",
                                 on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="following",
                                  on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
