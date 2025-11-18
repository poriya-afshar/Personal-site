from django.contrib import admin
from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'created_at']
    search_fields = ['title', 'content', 'author']
    list_filter = ['created_at', 'author']
    readonly_fields = ['created_at']

    # slug رو خودکار پر میکنه (اختیاری)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'text']
    readonly_fields = ['created_at']