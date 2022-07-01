from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    descripcion = RichTextField(null=True)
    contenido = RichTextField(blank=True, null=True)
    imagen=models.ImageField(upload_to="imagenes")
    fecha = models.DateTimeField()

    class Meta:
        ordering = ('-fecha',)

    def __str__(self):
        return self.titulo + "| fecha: " + str (self.fecha)
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=False, blank=False)
    email = models.EmailField()
    contenido = RichTextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.post)  + ' | ' + str( self.fecha)

    

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatares', null=True, blank=True,default='avatares/loginDefault.jpg')

    def __str__(self):
        return self.image.name

