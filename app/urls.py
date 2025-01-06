from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin-page/", views.admin, name="admin"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logoutpage, name="logoutpage"),
    path("register/", views.register, name="register"),

]
