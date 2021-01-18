from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_body = models.TextField()
    blog_image = models.ImageField()

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None) # blog is associated with a user 

    blog_created_on = models.DateTimeField(auto_now_add=True)
    blog_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
