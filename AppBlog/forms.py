from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar")
    password1 =forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 =forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    #es una clase interna que solamente contiene metadata que esta unida a nuestro formulario
    class Meta:
        model= User
        fields=["email", "password1", "password2"]
        help_text ={k:"" for k in fields}
"""

class UserEditForm(UserCreationForm):
    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Mensajes de ayuda
        help_texts = {k:"" for k in fields}