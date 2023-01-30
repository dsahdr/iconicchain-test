from django.urls import path
from knox import views as knox_views

from src.users.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
]
