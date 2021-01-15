from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("home/", views.home, name = 'home' ),
    path("viewPost/<int:pk>", views.viewPost, name = 'viewPost' ),
    path("viewAllPosts/", views.viewAllPosts, name = 'viewAllPosts' ),
]
