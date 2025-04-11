from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('post/<int:pk>/comments/new/', views.post_detail, name='post-comment'),  
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'), 
]
