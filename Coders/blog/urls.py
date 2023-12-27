from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs',views.blogs,name='blogs'),
    path('blogpost/', views.blogpost, name='blogpost'),  # Updated URL pattern
    path('blogpost/<str:slug>/', views.blogpost, name='blogpost_with_slug'),
    path('Contact',views.Contact,name='Contact'),
    path('Search',views.Search,name='Search')

]
