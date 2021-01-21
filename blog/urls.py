from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("home/", views.home, name = 'home' ),
    path("ajaxPostBlog/", views.ajaxPostBlog, name = 'ajaxPostBlog' ),
    path("viewPost/<int:pk>", views.viewPost, name = 'viewPost' ),
    path("editPost/<int:pk>", views.editPost, name = 'editPost' ),
    path("deletePost/<int:pk>", views.deletePost, name = 'deletePost' ),
    path("viewAllPosts/", views.viewAllPosts, name = 'viewAllPosts' ),
]
