from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-blog', views.add_blog, name='add_blog'),
    path('blog-info/<int:blog_id>', views.blog_info, name='blog_info'),
]
