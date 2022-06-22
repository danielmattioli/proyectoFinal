from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    contenido = RichTextField(blank=True, null=True)
    fecha = models.DateTimeField()
    class Meta:
        ordering = ('-fecha',)
        

    def __str__(self):
        return self.titulo
    
    
class Comentario(models.Model):
    Post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="Comentarios", null=True, blank=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    contenido = RichTextField(blank=True, null=True)
    fecha = models.DateTimeField()
    
    def __str__(self):
        return self.nombre  + ' | ' + str( self.Post)

    

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return self.image.name

