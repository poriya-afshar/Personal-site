from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # برای /blog/
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # برای /blog/post-slug/
]