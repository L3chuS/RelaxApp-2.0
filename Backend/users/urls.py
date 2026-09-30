from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("register/", views.user_registration, name="user_registration"),
    path("reset/", views.user_pw_reset, name="user_pw_reset"),
    path("reset/confirm/", views.user_pw_reset_confirmation, name="user_pw_reset_confirmation"),
    path("profiles/", views.profiles, name="profiles"),
    path("profiles/<int:pk>/", views.profile_details, name="profile_details"),
    path("data/validate/", views.data_validate, name="data_validate"),
    path("account/remove/", views.remove_account, name="remove_account")
]
