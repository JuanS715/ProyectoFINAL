from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[path("",index, name="index1"),
             path("index/",index, name="index"),
             path("about/", about, name="about"),
             path("posts/", allPosts, name="posts"),
             path("register/", register, name="register"),
             path("login/", login_a, name="login"),
             path("logout/", LogoutView.as_view(), name='logout'),
             path("myposts/", postForm, name="myposts"),
             path("buscar/", buscar, name="buscar"),
             path("postsFinder/", postsFinder, name="postsfinder"),
             path("profile/", editUser, name="profile"),
             path("avatar/", agregarAvatar, name="agregarAvatar"),
             path("postscompleto/", allPosts, name="postsCompleto"),
             path('message/', include("message.urls")),]