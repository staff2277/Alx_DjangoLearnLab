from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .templates.relationship_app import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Q2 function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # Q2 class-based view
    path("register/", views.register, name="register"),  # Q3 user registration
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # Q3 user login
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # Q3 user logout
]
