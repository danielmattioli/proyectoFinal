from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone


#class Comentario(models.Model):



class Categoria(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    contenido = models.TextField()