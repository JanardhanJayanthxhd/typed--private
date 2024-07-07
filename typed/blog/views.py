from django.shortcuts import render
from .models import Blog


def home(request):
    all_blogs = Blog.objects.order_by('updated_at')
    return render(request, 'blog/home.html',
                  {'blogs': all_blogs})
