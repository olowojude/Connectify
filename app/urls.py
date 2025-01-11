from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("admin-page/", views.admin, name="admin"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logoutpage, name="logoutpage"),
    path("register/", views.register, name="register"),
    path("add-link/", views.addlink, name="addlink"),
    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),
    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),
    re_path(r'^(?P<username>\w+)/$', views.preview, name="preview"),
    path("update-profile/", views.updateProfile, name="updateprofile"),
]
# URL patterns to serve static files during development
urlpatterns += staticfiles_urlpatterns()

# URL patterns to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
