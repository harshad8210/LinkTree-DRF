from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_verified', 'social_link_position',
              'theme_key']
