from django.http import HttpResponse
from AppBlog.forms import UserEditForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppBlog.forms import UserEditForm, PostForm
from AppBlog.models import Avatar, Post
from django.views.generic import ListView, DetailView



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
                avatar= Avatar.objects.filter(user=request.user.id)
                return render(request, "home.html", {"url":avatar[0].image.url})
                #return render(request, "home.html")
            else:
                return render(request, "errorlogin.html")
        else:
            return HttpResponse(f"LOGIN INCORRECTO")
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

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method =="POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.username=informacion["username"]
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "home.html")

    else:
        miFormulario=UserEditForm(initial={"email": usuario.email})
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario":usuario})


#Muestra los comentarios
class PostList(ListView):
    model = Post
    template_name = "listarPosteos.html"

class DetallePost(DetailView):
    modelo= Post
    template_name ="detallePosteos.html"


#muestro los post en el html    
#def post_list(request):
#    posts = Post.objects.filter(fecha__lte=timezone.now()).order_by('-fecha')
#    return render(request, 'paginas.html', {'posts': posts, 'bandera':'true'})


#guardo nuevos post a la db
@login_required
def NuevoPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guardadoExitoso')
            #return HttpResponse("joya")
    else:
        form = PostForm()
    return render(request, 'nuevo_post.html', {'form': form})

@login_required
def listo(request):
    return render(request, "guardadoExitoso.html")

def contacto(request):
    return render (request, "contacto.html")




@login_required
def eliminar(request, idpost):
    if request.method == "POST":
        try:
            form= Post.objects.filter(id=idpost)
            form.delete()
            return redirect('eliminadoExitoso')
        except:
            return render(request, 'eliminadoExitoso.html')
    else:
        form = Post.objects.filter(id=idpost)
    return render(request, 'eliminarPost.html', {'form': form})

@login_required
def eliminadoOk(request):
    return render(request, "eliminadoExitoso.html")

