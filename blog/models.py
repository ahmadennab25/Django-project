from django.db import models
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,   # keep the post even if the user is gone
        related_name='posts',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,   # keep the post even if its category is gone
        related_name='posts',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# COMMENT - another one-to-many (one post has many comments)
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,   # keep the comment even if the post is gone
        related_name='comments',
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,   # keep the comment even if the user is gone
        related_name='comments',
        null=True,
        blank=True,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.name if self.user else "Deleted User"} on {self.post.title if self.post else "Deleted Post"}'