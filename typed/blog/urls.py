from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-blog', views.add_blog, name='add_blog'),
    path('blog-info/<int:blog_id>', views.blog_info, name='blog_info'),
    path('edit-blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('delete-blog/<int:blog_id>', views.delete_blog, name='delete_blog')
]
