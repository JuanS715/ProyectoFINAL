from django.shortcuts import render
from .models import *
from .forms import  MessageForm

def correoPadre(request):
    return render(request,"global/correoPadre.html", )
   
 
# Create your views here.
def messages(request):
    if request.method=="POST":
        form=MessageForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            receptor=info["receptor"]
            mensaje=info["mensaje"]
            contenido=Mensaje(receptor=receptor, mensaje=mensaje)
            contenido.save()
            return render(request, "global/index.html" ,{"mensaje":"Mensaje enviado correctamente"})
        else:
            return render(request,"global/message.html", {"form":form})


    else:
        form=MessageForm()
        return render(request, "global/message.html",{"form":form})

def showMessages(request):
    usuarios=request.user
    email=usuarios.email
    
    if email!="":
        mensajes=Mensaje.objects.filter(receptor = email)
        return render (request, "global/showMessage.html", {"mensajes":mensajes} )
    else:
         return render(request, "global/message.html", {"mensaje":"Try Again "})