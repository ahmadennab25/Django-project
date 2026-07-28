from django.db import models

from .category import Category

class Topic (models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=150)