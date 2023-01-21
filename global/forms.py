from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="User Email")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    username=forms.CharField(label="Username")


    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_text={k:"" for k in fields}


class EditUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="User Email")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Informacion persnal NOMBRE")
    last_name=forms.CharField(label="Informacion personal APELLIDO")
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_text={k:"" for k in fields}

class PostsForm(forms.Form):
    titulo=forms.CharField(label="Titulo",max_length=30)
    post=forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    subtitulo=forms.CharField(label="Subtitulo",max_length=30)
    autor=forms.CharField(label="Autor",max_length=30)
    fecha=forms.DateField(label="Fecha")
    previewPost=forms.CharField(widget=forms.Textarea(attrs={"rows":"2"}))
    
    

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
