from django.contrib import admin
from links.models import Link, UserLink

# Register Link and UserLink model to admin site
admin.site.register(Link)
admin.site.register(UserLink)
