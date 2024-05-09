from django.db import models
from login.models import User


class SocialIcons(models.Model):
    """Social Icons Model"""
    name = models.CharField(max_length=50)


class UserSocials(models.Model):
    """User Social Model"""
    user = models.ForeignKey(User, related_name='social', on_delete=models.CASCADE)
    social_icon = models.ForeignKey(SocialIcons, related_name='icon', on_delete=models.CASCADE)
    links = models.CharField(max_length=50)
    position = models.IntegerField(null=True, unique=True)

    class Meta:
        unique_together = ('user', 'social_icon',)
        ordering = ['position']
