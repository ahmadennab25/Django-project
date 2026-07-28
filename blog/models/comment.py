from django.db import models

from .post import Post
from .user import User

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