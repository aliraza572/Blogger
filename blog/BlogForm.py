from django import forms

class BlogForm(forms.Form):
    blog_title = forms.CharField()
    blog_body = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})
    blog_image = forms.ImageField()
