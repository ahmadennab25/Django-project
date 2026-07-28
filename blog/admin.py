#from django.contrib import admin
#from .models import  Post
from django.contrib import admin
from .models import User, Post, Comment


# ModelAdmin fits - NOT the auth UserAdmin.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'is_active', 'created_at')
    search_fields = ('name', 'phone_number')
    list_filter = ('is_active', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_published', 'created_at')
    search_fields = ('title', 'user__name')
    list_filter = ('is_published', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'created_at')
    search_fields = ('user__name', 'post__title')
    list_filter = ('created_at',)