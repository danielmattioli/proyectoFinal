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
    #Muestra los posteos
    path("listarPosteos/", PostList.as_view(),name="listarPosteos"),
    #otra forma de listar post
    #path('listarPost', views.post_list, name='listarPost'), 
    #crea nuevo post
    path('nuevoPost/', views.NuevoPost, name='nuevoPost'),
    path('guardadoExitoso', listo, name = 'guardadoExitoso'),
    path("contacto", views.contacto, name="contacto"),
    path("eliminarPosteo/<int:idpost>", views.eliminar,name="eliminarPosteo"),
    path('eliminadoExitoso', views.eliminadoOk),
    


    #falta editar post
    #ver posteo en pantalla completa con la opcion de comentar
    #falta comentar un post
    #mensajes entre usuarios
    



]
