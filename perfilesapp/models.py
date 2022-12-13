
from ast import AugStore
from tkinter import image_names
from turtle import title
from django.db import models
from django.contrib.auth.models import User

#from pyparsing import null_debug_action

# Create your models here.

class Avatar(models.Model):

    usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    imagen= models.ImageField("imagen", upload_to= "avatar/", blank=True, null=True)


class TiendaActividad(models.Model):
    ACTIVIDAD=(
        ("Curso Individual", "Curso individual"),
        ("Curso para dos", "Curso para dos"),
        ("Curso para cuatro", "Curso para cuatro"), 
        ("Salida en trainera", "Salida en trainera"),
    )
    actividad= models.CharField("Actividad", choices=ACTIVIDAD, max_length=30)
    profesor= models.CharField("NombreProfesor", max_length=30)
    dias= models.CharField("Dias", max_length=30)
    TURNOS=(
        ("mañana", "mañana"),
        ("tarde", "tarde"),
        
    )
    turno= models.CharField("Turno", choices=TURNOS, max_length=30)
    precio= models.FloatField("Precio $")
    imagen = models.ImageField("Imagen", upload_to="objetos/", null=True, blank = True) # despues de que todo tenga imagen puedo comentar , null=True, blank=True
    
    class Meta:
        verbose_name_plural = "Tienda de Actividades"
    
class TiendaObjetos(models.Model):
    
    producto = models.CharField("Producto", max_length=30)
    descripcion = models.CharField("Descripcion Producto", max_length=150)
    precio = models.FloatField("Precio $")
    imagen = models.ImageField("Imagen", upload_to="objetos/", null=True, blank=True) # despues de que todo tenga imagen puedo comentar , null=True, blank=True
    
    class Meta:
        verbose_name_plural = "Tienda de Objetos"
        


class Socios(models.Model):
    nombre = models.CharField("Nombre Socio", max_length=30)
    apellido = models.CharField("Apellido Socio", max_length=30)
    edad = models.SmallIntegerField("Edad")
    fechanacimiento = models.DateField("Fecha de Nacimiento")
    email = models.EmailField("E-mail")

        
    class Meta:
        verbose_name_plural = "Socios"
    #foto
    
class Profesor(models.Model):
    nombreprofesor = models.CharField("Nombre Profesor", max_length=30)
    apellidoprofesor = models.CharField("Apellido Profesor", max_length=30)
    edadprofesor = models.SmallIntegerField("Edad")
    emailprofesor = models.EmailField("E-mail")
    
    class Meta:
        verbose_name_plural = "Profesores"
    #foto

class Blog(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    subtitulo = models.CharField("Subtitulo", max_length=30)
    texto = models.CharField("Texto", max_length=5000)
    imagen = models.ImageField("Imagen", upload_to="blog/", null=True, blank=True)   
    user= models.ForeignKey(User, verbose_name="Usuario", null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    fecha = models.DateTimeField(auto_now=True, verbose_name="Fecha" )

class Comentario(models.Model):
    blog= models.ForeignKey(Blog, verbose_name="Blog", null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    nombre= models.CharField("Nombre", max_length=15)
    comentario= models.CharField("Comentario", max_length=500)






