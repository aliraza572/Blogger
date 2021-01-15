from django.shortcuts import render
from.BlogForm import *

def home(request):
    context = {}
    context['form'] = BlogForm()
    return render(request, "blog/home.html", context)