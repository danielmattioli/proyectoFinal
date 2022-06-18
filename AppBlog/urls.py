from django.contrib import admin
from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name = "home"),
    path("paginas", views.paginas, name = "paginas"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarperfil", views.editarPerfil, name="editarperfil"),

]
