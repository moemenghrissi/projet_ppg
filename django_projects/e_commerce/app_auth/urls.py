from django.urls import path
from .views import login_blog
from . import views

urlpatterns = [
    path('login', views.login_blog, name='login_blog'),


]