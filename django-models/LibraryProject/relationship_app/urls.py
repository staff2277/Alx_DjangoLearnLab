from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
]
