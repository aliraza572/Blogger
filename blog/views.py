from django.shortcuts import render,redirect, get_object_or_404
from .forms import *

def home(request):
    context = {}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_title = form.cleaned_data["blog_title"]
            blog_body = form.cleaned_data["blog_body"]
            blog_image = form.cleaned_data["blog_image"]
            post=form.save()
            # blog_obj = BlogPost.objects.create(blog_title=blog_title, blog_body = blog_body, blog_image= blog_image )
            # blog_obj.save()
            # print(blog_obj)
            return redirect('blog:viewPost', post.id)
        else:
            context['form'] = form
            return render(request, "blog/home.html", context)
    else:
        blog_form = BlogForm()

    context['form'] = blog_form
    return render(request, "blog/home.html", context)


def viewPost(request, pk):
    # print(pk)
    obj = get_object_or_404(BlogPost, pk = pk)
    # print(obj)
    context = {'blog_obj' : obj}
    return render(request, 'blog/blog_detail.html', context)


def viewAllPosts(request):
    obj = BlogPost.objects.all()
    return render(request, "blog/all_blogs.html", {'all_blogs' : obj})


def deletePost(request, pk):
    obj = get_object_or_404(BlogPost, pk = pk)
    print(obj)
    obj.delete()
    # context = {'blog_obj' : obj}
    return redirect('blog:viewAllPosts')


def editPost(request, pk):
    if request.method == "POST":
        # print("update part here")
        obj = get_object_or_404(BlogPost, pk = pk)
        # print(obj.id)
        form = BlogForm(request.POST, request.FILES, instance=obj)
        if form.is_valid:
            form.save()
            return redirect("blog:viewPost", pk=pk)
        else:
            return render(request, "blog/edit_post.html", {'form:obj'})
    else:
        obj = get_object_or_404(BlogPost, pk = pk)
        # print("here")
        # print(obj.id)
        return render(request, "blog/edit_post.html", {'form' : obj})


# def updatePost(request, pk):
#     print("update part here")
#     obj = get_object_or_404(BlogPost, pk = pk)
#     print(obj.id)
#     form = BlogForm(request.POST, instance=obj)
#     if form.is_valid:
#         form.save()
#         return redirect("blog:viewPost")
#     else:
#         return render(request, "blog/edit_post.html", {'form:obj'})
