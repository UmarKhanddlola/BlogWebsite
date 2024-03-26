from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact/', views.contact, name="contact"),
]
