from django.contrib import admin

# Register your models here.
from .models import Post
from organizer.models import Medlem


admin.site.register(Post)
admin.site.register(Medlem)
