from django.urls import path
from . import views

urlpatterns = [
    # READ - List all posts
    path('', views.post_list, name='post_list'),
    
    # READ - Detail of a post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # CREATE - Create a new post
    path('post/new/', views.post_create, name='post_create'),
    
    # UPDATE - Edit a post
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    
    # DELETE - Delete a post
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
