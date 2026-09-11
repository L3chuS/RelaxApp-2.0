from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("register/", views.user_registration, name="user_registration"),
    path("reset/", views.user_pw_reset, name="user_pw_reset"),
    path("reset/confirm/", views.user_pw_reset_confirmation, name="user_pw_reset_confirmation"),
]
