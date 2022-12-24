from django.contrib import admin

# Register your models here.
from .models import *



#admin.site.register(Category)
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
