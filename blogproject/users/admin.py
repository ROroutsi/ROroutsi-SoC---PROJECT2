from django.contrib import admin
from .models import comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentAuthor', 'commentBlog',
                    'commentDate')


admin.site.register(comment, CommentAdmin)
