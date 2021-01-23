from django.urls import path
from .views import (
    ListArticles,
    DetailArticle,
    ArticleCreate,
    DeleteArticle,
    UpdateArticle,
    contact,
    handelLogout,
    handeLogin,
    handleSignUp,
    about,
    home
    )

urlpatterns = [
    path('',home,name="home"),
    path('login',handeLogin, name="handleLogin"),
    path('logout',handelLogout, name="handleLogout"),
    path('signup',handleSignUp, name="handleSignUp"),
    path('list/',ListArticles.as_view(),name = "home"),
    path('detail/<int:pk>',DetailArticle.as_view(),name = "detail"),
    path('create/',ArticleCreate.as_view(),name = "create"),
    path('delete/<pk>/', DeleteArticle.as_view(),name="delete"), 
    path('update/<int:pk>', UpdateArticle.as_view(),name="update"), 
    path('contact/',contact,name="contact"),
    path('about/', about, name="about"),
]
