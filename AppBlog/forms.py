from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Comentario, Post


class UserEditForm(UserCreationForm):
    #Acá se definen las opciones que queres modificar del usuario
    username=forms.CharField(label="Modificar nombre de usuario")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ "username", 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields} #Mensajes de ayuda

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=("categoria", "titulo", "descripcion", "contenido", "fecha", "imagen",)


class ComentForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['usuario',]
        
        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control', "type":"hidden"}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
            }
        

class Coment_crear(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=("contenido", )

