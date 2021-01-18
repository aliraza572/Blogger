from django import forms
from blog.models import *

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('blog_title', 'blog_image', 'blog_body')
    