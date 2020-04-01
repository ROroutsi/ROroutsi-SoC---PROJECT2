from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class comment(models.Model):

    commentAuthor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commentAuthor')
    commentBlog = models.ForeignKey(
        'blogs.blog', on_delete=models.CASCADE, related_name='commentBlog')
    commentContent = models.TextField()
    commentDate = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ["-commentDate"]
