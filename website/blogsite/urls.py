from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('index/', views.index, name="blog-index"),
]
