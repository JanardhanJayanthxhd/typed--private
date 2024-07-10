from .models import Blog, Category
from django.forms import ModelForm
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(),
        }

