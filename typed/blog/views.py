from django.shortcuts import render
from .models import Blog


def home(request):
    all_blogs = Blog
    return render(request, 'blog/home.html',
                  {})
