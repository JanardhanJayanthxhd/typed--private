from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField('Tag', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(Category, related_name='blogs')

    title = models.CharField('BLog Title', max_length=150, null=False, blank=False)
    content = RichTextField('Content', blank=True, null=True, config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    objects = models.Manager()

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    comment = models.TextField('Comment', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]

