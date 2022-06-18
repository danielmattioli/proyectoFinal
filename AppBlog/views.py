from django.http import HttpResponse
from AppBlog.forms import UserEditForm
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppBlog.forms import UserEditForm
from AppBlog.models import Avatar

# Create your views here.
def home(request):
    return render(request, "home.html")
    
def paginas(request):
    return render(request, "paginas.html")

def login_request(request):
    if request.method =="POST":
        
        #se genera un formulario con la data que mando el usuario por medio del request
        form= AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user= authenticate(username= usuario, password=contra)
            
            if user is not None:
                login(request,user)
                #avatar= Avatar.objects.filter(user=request.user.id)
                
                #return render(request, "home.html", {"url":avatar[0].imagen.url})
                #retorna la pagina de los post junto con un mensaje
                return render(request,"paginas.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request, "errorlogin.html")
        else:
            return HttpResponse(f"LOGIN INCORRECTO {form}")
    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})

#registro de usuarios nuevos
def register(request):
    if request.method== "POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render (request, "registrook.html")
    else:
        form= UserCreationForm()
    return render( request, "registro.html", {"form":form})


def editarPerfil(request):
    usuario = request.user
    if request.method =="POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "home.html")

    else:
        miFormulario=UserEditForm(initial={"email": usuario.email})
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario":usuario})
