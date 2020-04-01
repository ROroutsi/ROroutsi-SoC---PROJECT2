from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class blog(models.Model):

    blogTitle = models.CharField(max_length=200, unique=True)
    blogSlug = models.SlugField(max_length=200, unique=True)
    blogContent = models.TextField()
    blogLikes = models.ManyToManyField(
        User, related_name='blogLikes', blank=True)
    blogDate = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        ordering = ["-blogDate"]

    def __str__(self):
        return self.blogTitle

    def totalLikes(self):
        return self.blogLikes.count()

    def get_absolute_url(self):
        return reverse("slug", args=[self.id, self.blogSlug])
