from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.home, name="home"),
    path("admin-page/", views.admin, name="admin"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logoutpage, name="logoutpage"),
    path("register/", views.register, name="register"),
    path("add-link/", views.addlink, name="addlink"),
    path("update-link/<str:pk>/", views.updatelink, name="updatelink"),
    path("delete-link/<str:pk>/", views.deletelink, name="deletelink"),
    re_path(r'^(?P<username>[a-zA-Z0-9._-]+)/$', views.preview, name="preview"),
    path("update-profile/", views.updateProfile, name="updateprofile"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="password-reset-page.html"),
         name="reset_password"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="lta/password-reset-form-page.html"),
         name="password_reset_confirm"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-sent-page.html"),
         name="password_reset_done"),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete-page.html"),
         name="password_reset_complete")
]
# URL patterns to serve static files during development
urlpatterns += staticfiles_urlpatterns()

# URL patterns to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
