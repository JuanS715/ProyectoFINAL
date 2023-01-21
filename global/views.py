from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login_procces, authenticate
from .forms import PostsForm, RegistroUsuarioForm, EditUsuarioForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="media/avatars/avatarpordefecto.png"
    return avatar

# Create your views here.
def index(request):
    return render(request, "global/index.html", )
def posts(request):
    return render(request,"global/posts.html")
def about(request):
    return render(request,"global/about.html")
def register(request):
    return render(request, "global/register.html")
def login(request):
    return render(request, "global/login.html")
def myposts(request):
    return render(request, "global/myposts.html", {"avatar":obtenerAvatar(request)})
def postsFinder(request):
    return render(request, "global/postsFinder.html", {"avatar":obtenerAvatar(request)})
  

# activity renders
def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            
            form.save()
            return render(request, "global/index.html", {"mensaje":"Usuario creado correctamente"})
        else:
            return render(request, "global/register.html", {"form":form, "mensaje":"Ups! hubo un error intentelo nuevamente"} )
    else:
        form=RegistroUsuarioForm()
        return render(request, "global/register.html", {"form":form})

def login_a(request):
    if request.method=="POST":
       form=AuthenticationForm(request, data=request.POST)
       if form.is_valid():
        info=form.cleaned_data
        usu=info["username"]
        contra=info["password"]
        usuarios=authenticate(username=usu, password=contra)
        if usuarios is not None:
            login_procces(request,usuarios)
            return render(request, "global/index.html", {"mensaje":f"Bienvenido {usu}"})
        else:
            return render(request, "global/login.html", {"form":form, "Mensaje":"Usuario o contraseña incorrecto"})

       else:
            return render(request, "global/login.html", {"form":form, "Mensaje":"Usuario o contraseña incorrecto"})


    else:
        form=AuthenticationForm()
        return render(request, "global/login.html", {"form":form})

def postForm(request):
    if request.method=="POST":
        form=PostsForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["titulo"]
            post=info["post"]
            subtitulo=info["subtitulo"]
            autor=info["autor"]
            fecha=info["fecha"]
            previewPost=info["previewPost"]
            
            posteo=Post(titulo=titulo, post=post, subtitulo=subtitulo, autor=autor, fecha=fecha, previewPost=previewPost, )
            posteo.save()
            return render(request, "global/index.html",{"mensaje":"Post creado exitosamente"})
        else:
            return render(request, "global/myposts.html", {"form":form, "mensaje":"Try again"})

    else:
         form=PostsForm()
         return render(request, "global/myposts.html", {"form":form, "avatar":obtenerAvatar(request)}, )



@login_required
def buscar(request):
    titulo=request.GET["titulo"]
    
    if titulo !="": 
      posts=Post.objects.filter(titulo__icontains=titulo)
    

      return render(request, "global/postcompleto.html", {"posts":posts} )    
           
     
      
    else:
      return render(request, "global/index.html", {"mensaje":"Ocurrio un error en su busqueda intente nuevamente", "avatar":obtenerAvatar(request)})


def allPosts(request):
    posts=Post.objects.all()
    return render(request, "global/posts.html", {"posts":posts})

@login_required
def editUser(request):
    usuarios=request.user
    if request.method=="POST":
        form=EditUsuarioForm(request.POST)
        if form.is_valid():
         info=form.cleaned_data
         usuarios.email=info["email"]
         usuarios.password1=info["password1"]
         usuarios.password2=info["password2"]
         usuarios.first_name=info["first_name"]
         usuarios.last_name=info["last_name"]
         usuarios.save()
         
         return render(request,"global/index.html", {"mensaje":"Usuario editado correctamente"})
        else:
            return render(request,"global/profile.html", {"form":form})
    else:
        form=EditUsuarioForm(instance=usuarios)
        return render(request,"global/profile.html", {"form":form, "avatar":obtenerAvatar(request)})

def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete 
            avatar.save()
            return render(request, "global/index.html")
        else:
            return render(request, "global/avatar.html", {"form":form, "usuario":request.user, "mensaje":"ocurrio un error intente nuevamente"})

    else:
        form=AvatarForm()
        return render(request, "global/avatar.html", {"form":form, "usuario":request.user})



   