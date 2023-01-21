from django.db import models

# Create your models here.
class Mensaje(models.Model):
    receptor=models.EmailField(max_length=30)
    mensaje=models.TextField(max_length=4000)
    