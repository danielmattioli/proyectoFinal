from django.contrib import admin
from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView
from .views import PostList, listo

urlpatterns = [
    path('', views.home, name = "home"),
    path("paginas", views.paginas, name = "paginas"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="home.html"), name="logout"),
    path("editarperfil", views.editarPerfil, name="editarperfil"),
    #path("verPosteo", views.verPosteo, name="verPosteo"),
    path("verposteo/", PostList.as_view(),name="verposteo"),
    #path("formulario_nuevoPost",views.formulario_nuevoPost, name="nuevoPost"),
    path('nuevoPost/', views.NuevoPost, name='nuevoPost'),
    path('guardadoExitoso', listo, name = 'guardadoExitoso'),
    path('listarPost', views.post_list, name='listarPost'),



]
