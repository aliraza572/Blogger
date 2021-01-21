from django import forms
from blog.models import *

class BlogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog_title'].widget.attrs.update({'class': 'form-control-lg', 'id': 'blogTitleLabel'})
        self.fields['blog_image'].widget.attrs.update({'class': 'form-control-file', 'id': 'blogImageLabel'})
        self.fields['blog_body'].widget.attrs.update({'class': 'form-control', 'id':'blogBodyLabel'})

    class Meta:
        model = BlogPost
        fields = ('blog_title', 'blog_image', 'blog_body')
    