from django.db import models
from login.models import User


class Link(models.Model):
    """Link Model"""
    name = models.CharField(max_length=50)


class UserLink(models.Model):
    """User Link Model"""
    user = models.ForeignKey(User, related_name='link_user', on_delete=models.CASCADE)
    link_key = models.ForeignKey(Link, related_name='link_name', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    links = models.URLField(max_length=400)
    position = models.IntegerField(unique=True, null=True)
    thumbnail_url = models.URLField(max_length=400, null=True)

    class Meta:
        unique_together = ('user', 'link_key',)
