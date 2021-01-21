from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def home(request):
    context = {}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # blog_title = form.cleaned_data["blog_title"]
            # blog_body = form.cleaned_data["blog_body"]
            # blog_image = form.cleaned_data["blog_image"]

            post = form.save(commit=False)
            post.user = request.user
            post.save()
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


def ajaxPostBlog(request):
    context = {}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            obj = BlogPost.objects.filter(username=request.user)
            return JsonResponse({'status':200, 'data':obj}) # if form is valid then send OK
        return JsonResponse({'status':400, 'data':form})
        


@login_required
def viewPost(request, pk):
    # print(pk)
    obj = get_object_or_404(BlogPost, pk=pk)
    if obj.user == request.user:
        # print(obj)
        context = {'blog_obj': obj}
    else:
        return HttpResponse("404")
    return render(request, 'blog/blog_detail.html', context)


@login_required
def viewAllPosts(request):
    obj = BlogPost.objects.filter(user=request.user)
    return render(request, "blog/all_blogs.html", {'all_blogs': obj})


@login_required
def deletePost(request, pk):
    obj = get_object_or_404(BlogPost, pk=pk)
    print(obj)
    obj.delete()
    # context = {'blog_obj' : obj}
    return redirect('blog:viewAllPosts')


@login_required
def editPost(request, pk):
    if request.method == "POST":
        # print("update part here")
        obj = get_object_or_404(BlogPost, pk=pk)
        # print(obj.id)
        form = BlogForm(request.POST, request.FILES, instance=obj)
        if form.is_valid:
            form.save()
            return redirect("blog:viewPost", pk=pk)
        else:
            return render(request, "blog/edit_post.html", {'form:obj'})
    else:
        obj = get_object_or_404(BlogPost, pk=pk)
        # print("here")
        # print(obj.id)
        return render(request, "blog/edit_post.html", {'form': obj})
