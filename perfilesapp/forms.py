
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class ProfesorFormulario(forms.Form):   
    nombreprofesor= forms.CharField(max_length=30, label="Nombre")
    apellidoprofesor= forms.CharField(max_length=30, label="Apellido")
    emailprofesor= forms.EmailField(label="Email")
    edadprofesor=forms.IntegerField(label="Edad")

class SocioFormulario(forms.Form):
    nombre = forms.CharField( max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30, label="Apellido")
    edad = forms.IntegerField( label= "Edad")
    fechanacimiento = forms.DateField(label= "Fecha de Nacimiento")
    email = forms.EmailField(label= "E-mail")

class ObjetoFormulario(forms.Form):

    producto = forms.CharField( max_length=30, label="Producto")
    descripcion = forms.CharField(max_length=150, label="Descripcion")
    precio = forms.IntegerField( label= "Precio")
    imagen = forms.ImageField(label= "Imagen", required=False)

    class Meta:
        model = TiendaObjetos
        fields = ['producto', 'descripcion', 'precio', 'imagen']
    
   # def save(self, commit=True):
   #      objeto = super(ObjetoFormulario, self).save(commit=False)
   #      objeto.producto = self.cleaned_data['producto']
   #      objeto.descripcion = self.cleaned_data['descripcion']
   #      objeto.precio = self.cleaned_data['precio']
   #      objeto.imagen = self.cleaned_data['imagen']
   #      if commit:
   #          objeto.save()
   #      return objeto


class CursoFormulario(forms.Form):
    ACTIVIDADES=( ("Curso individual", "Curso individual"),
        ("Curso para dos", "Curso para dos"),
        ("Curso para cuatro", "Curso para cuatro"), 
        ("Salida en trainera", "Salida en trainera"),
    )
    TURNOS=(
        ("mañana", "mañana"),
        ("tarde", "tarde"), 
    )
    actividad = forms.CharField( label="Actividad", widget=forms.Select(choices=ACTIVIDADES))
    profesor = forms.CharField(max_length=30, label="Profesor")
    dias = forms.CharField( label= "Dias")
    turno = forms.CharField(label= "Turno", widget=forms.Select(choices=TURNOS))
    precio = forms.IntegerField(label= "Precio")
    imagen = forms.ImageField(label= "Imagen", required=False) ##################
    
    class Meta():
        model = TiendaActividad
        fields = ['actividad', 'profesor', 'dias', 'turno', 'precio', 'imagen']
    

class UserRegisterForm(UserCreationForm):
        
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
            
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen", required = False)
class Meta:
    model= Avatar
    fields = ["imagen"]

class BlogForm(forms.Form):
    titulo = forms.CharField(label="Titulo")
    subtitulo = forms.CharField(label="Subtitulo")
    texto = forms.CharField(widget=forms.Textarea, label="Texto")
    imagen = forms.ImageField(label="Imagen", required=False) #agregue el required=False
    fecha = forms.DateTimeField(label="Fecha", required=False)

    class Meta:
        model= Blog
        fields= ['titulo', 'subtitulo', 'texto', 'imagen', 'fecha']

class ComentarioForm(forms.Form):
    nombre= forms.CharField(label="Nombre")
    comentario= forms.CharField(label="Comentario")

    class Meta:
        model = Comentario
        fields = ('nombre', 'comentario')
        