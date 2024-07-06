from django.contrib import admin
from .models import Blog, Category, Comment


admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Blog)
class ViewBlog(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)

