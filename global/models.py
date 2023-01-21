from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=30)
    post=models.TextField(max_length=4000)
    subtitulo=models.CharField(max_length=60)
    autor=models.CharField(max_length=30)
    fecha=models.DateField()
    previewPost=models.CharField(max_length=1000)
    
    def __str__(self):
        template="{0.titulo}{0.post}{0.subtitulo}{0.autor}{0.fecha}{0.previewPost}"
        return template.format(self)

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    