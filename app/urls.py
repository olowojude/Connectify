from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin-page/", views.admin, name="admin"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logoutpage, name="logoutpage"),
    path("register/", views.register, name="register"),
    path("add-link/", views.addlink, name="addlink"),
    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),
    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),
]
