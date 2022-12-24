from django.contrib import admin
from post.models import *


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'published']
# Register your models here.
