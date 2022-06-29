from django.contrib import admin
from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView
from .views import PostList, DetallePost, listo,listo2

urlpatterns = [
    path('', views.home, name = "home"),
    path("paginas", views.paginas, name = "paginas"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="home.html"), name="logout"),
    path("editarperfil", views.editarPerfil, name="editarperfil"),
    path("listarPosteos/", PostList.as_view(),name="listarPosteos"),
    #otra forma de listar post
    #path('listarPost', views.post_list, name='listarPost'), 
    path('nuevoPost/', views.NuevoPost, name='nuevoPost'),
    path('guardadoExitoso', listo, name = 'guardadoExitoso'),
    path('PosteoEditado', listo2, name="PosteoEditado"),
    path("contacto", views.contacto, name="contacto"),
    path("eliminarPosteo/<int:idpost>", views.eliminar,name="eliminarPosteo"),
    path('eliminadoExitoso', views.eliminadoOk),
    path("<int:id>/", DetallePost.as_view(), name="unposteo"),
    path("editarPosteos/<int:pk>", views.editarPosteo, name="editarPosteo"),
    
]

    #falta comentar un post
    #mensajes entre usuarios
