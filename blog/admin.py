from django.contrib import admin
from .models import BlogPage, BlogPageAuthor

# Register your models here.
admin.site.register(BlogPageAuthor)
admin.site.register(BlogPage)