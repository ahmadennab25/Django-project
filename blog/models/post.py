from django.db import models
from .user import User
from .category import Category


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    summary = models.TextField(blank=True, default='')
    summary_generated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title