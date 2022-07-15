from django.db import models

# Create your models here.

class empleados(models.Model):
    id=models.IntegerField
    nom=models.CharField(max_length=50)
    mail=models.EmailField()

class clientes(models.Model):
    id=models.IntegerField
    nom=models.CharField(max_length=50)
    mail=models.EmailField()

class proveedores(models.Model):
    id=models.IntegerField
    nom=models.CharField(max_length=50)   
    mail=models.EmailField()
