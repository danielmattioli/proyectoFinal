from django.contrib import admin
from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView
from .views import DetallePost, listo,listo2

urlpatterns = [
    path('', views.home, name = "home"),
    path("comentarios", views.comentarios, name = "comentarios"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="home.html"), name="logout"),
    path("editarperfil", views.editarPerfil, name="editarperfil"),
    #otra forma de listar post pero devo traer del from a PostList
    #path("listarPosteos/", PostList.as_view(),name="listarPosteos"),
    
    path('listarPosteos/', views.post_list, name='listarPosteos'), 
    path('nuevoPost/', views.NuevoPost, name='nuevoPost'),
    path('nuevoComentario/', views.nuevoComentario, name='nuevoComentario'),
    path('guardadoExitoso', listo, name = 'guardadoExitoso'),
    path('PosteoEditado', listo2, name="PosteoEditado"),
    path("contacto", views.contacto, name="contacto"),
    path("eliminarPosteo/<int:idpost>", views.eliminar,name="eliminarPosteo"),
    path('eliminadoExitoso', views.eliminadoOk),
    path("<int:id>/", DetallePost.as_view(), name="unposteo"),
    path("editarPosteos/<int:pk>", views.editarPosteo, name="editarPosteo"),
    path("comentarios/<int:pk>", views.listarComentarios, name="comentarios"),
    
]

    #falta comentar un post
    #mensajes entre usuarios
