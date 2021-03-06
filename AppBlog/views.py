from django.http import HttpResponse
from AppBlog.forms import UserEditForm, Coment_crear
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppBlog.forms import UserEditForm, PostForm, ComentForm
from AppBlog.models import Comentario, Post, Avatar
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, "home.html")
    
def aboutMe(request):
    return render(request, "aboutMe.html")
    
def comentarios(request):
    return render(request, "comentarios.html")

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
                #return render(request, "home.html",{"url":"AppBlog/asset/img/loginDefault.jpg"})
            else:
                return HttpResponse(f"usuario incorrecto2!")
        else:
            return render(request, "errorlogin.html")
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


#Lista TODOS los posteos
class PostList(ListView):
    model = Post
    template_name = "listarPosteos.html"
    ordering = ['-fecha']




#lista UN solo posteo
class DetallePost(DetailView):
    #modelo= Post
    template_name ="unPosteo.html"
    queryset=Post.objects.all()
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post,id=id_)

#muestro los post en el html    
def post_list(request):
    posts = Post.objects.filter(fecha__lte=timezone.now()).order_by('-fecha')
    return render(request, 'listarPosteos.html', {'posts': posts})


#guardo nuevos post a la db
@login_required
def NuevoPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guardadoExitoso')
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


def editarPosteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.cleaned_data
            post = form.save()
            post.save()
            return redirect('PosteoEditado')
    else:
        #crea el formulario y lo llena con los datos que tenia guardados del post
        form = PostForm(instance=post)
    return render(request, 'editarPosteo.html', {'form': form})

def listo2(request):
    return render(request, "modificacionExitosa.html")

def listo3(request):
    return render(request, "comentarioGuardado.html")

#lista los comentarios y se los manda a comentarios.html
def listarComentarios(request,pk):
    comentarios = Comentario.objects.filter(post_id=pk)
    print("pk=", pk)
    print(comentarios)
    return render(request, 'comentarios.html', {'coment': comentarios} )

"""
def nuevoComentario(request):
    if request.method == "POST":
        #guardo el usuario que viene de posteo
        autor=request.POST["usuario"]
        
        print("autor", autor)
        
        form = Coment_crear(request.POST)
        #print("miFormulario", miFormulario)
        
        if form.is_valid():
            form= form.cleaned_data
            #print(form)
            #miFormulario= ComentForm(usuario=autor, instance=form)
            #guardo usuario que viene del html
            #miFormulario.usuario = "usuario"
            #miFormulario.post
            #miFormulario.email = "email"
            #miFormulario.comentario = request.POST["contenido"]
            #miFormulario.fecha = request.POST["fecha"]
            
            #print(miFormulario)
            
            #miFormulario.save()
            #return redirect('comentarioGuardadoExitoso')
    else:
        form = Coment_crear()
    return render(request, 'nuevo_comentario.html', {'form': form})
"""


class NuevoComentario(CreateView):
    model = Comentario
    form_class: ComentForm
    template_name = "nuevo_comentario.html"
    fields= "__all__"
    #success_url: reverse_lazy('home')