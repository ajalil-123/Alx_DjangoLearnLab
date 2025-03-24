
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

from django.http import HttpResponse

#dummy post view
def dummy_view(request):
    return HttpResponse("This is a placeholder.")

#dummy register view
# def register_view(request):
#     return HttpResponse("This is the register page.")

urlpatterns = [
    
    path("", TemplateView.as_view(template_name="blog/home.html"), name="home"),
     path("posts/", dummy_view, name="posts"),
    #path('register/', register_view, name='register'),
    path('register/', views.register, name='register'),
]