from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm


def home(request):
    all_blogs = Blog.objects.order_by('updated_at')
    return render(request, 'blog/home.html',
                  {'blogs': all_blogs})


def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            category = request.POST['category']
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user_id = request.user.id
                blog.save()
                messages.success(request, 'blog added')
                return redirect('home')

        else:
            form = BlogForm()

        return render(request, 'blog/add_blog.html',
                      {'form': form})
    else:
        messages.success(request, 'Must be logged in to write blog.')
        return redirect('login_user')


def blog_info(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog_owner = blog.user
    print(blog.content, f'owner {blog_owner}')
    return render(request, 'blog/blog_info.html',
                  {'blog': blog, 'owner': blog_owner})
