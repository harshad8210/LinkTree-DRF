from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.dispatch import receiver

from login.manager import UserManager
from theme.models import Theme


class User(AbstractUser):
    """User model"""
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=45, unique=True)
    otp = models.CharField(max_length=6, default=None, null=True)
    is_verified = models.BooleanField(default=False)
    social_link_position = models.BooleanField(default=True)
    theme_key = models.ForeignKey(Theme, null=True, related_name='used_theme', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f"{reverse('password_reset:reset-password-request')}?token={reset_password_token.key}"

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Linktree"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
