from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView  # Explicit imports for Q2
from . import views  # Module import for Q3 (ensures "views.register" exists)

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Q2 function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Q2 class-based view
    path("register/", views.register, name="register"),  # Q3 user registration
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # Q3 user login
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # Q3 user logout
]
