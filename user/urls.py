from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', views.login_view, name = "login"),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout, name = "logout"),
]