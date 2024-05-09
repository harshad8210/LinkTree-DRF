import random
import string
from django.core.mail import send_mail
from django.conf import settings
from login.models import User


def generate_otp():
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return "".join(random.choice(char) for _ in range(6))


def send_otp_via_email(user_email):
    subject = "Reminder: Verify your email to activate your Linktree"
    otp = generate_otp()
    message = f"Linktree account verification OTP is {otp}."
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [user_email])
    return otp


