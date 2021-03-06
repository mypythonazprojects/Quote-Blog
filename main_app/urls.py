"""simplequote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views

urlpatterns = [
    #path('', views.homeView, name="home"),
    #path('home/', views.homeView, name="home"),
    path('', views.HomeView.as_view(), name="home"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),   #don't forget to add , comma after path to add new path
    path('delete/<id>/', views.HomeView.deleteq, name="delete"), #define method don't need paranthese
    path('edit/<id>/', views.HomeView.editq, name="edit"),
    path('update/<id>/', views.HomeView.updateq, name="update")
]
