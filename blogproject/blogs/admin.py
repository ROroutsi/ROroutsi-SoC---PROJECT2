from django.contrib import admin
from .models import blog

admin.site.site_header = "Django Blog Admin"
admin.site.site_title = "Django Blog Admin Area"


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blogTitle', 'blogSlug',
                    'blogDate', 'totalLikes')


admin.site.register(blog, BlogAdmin)
