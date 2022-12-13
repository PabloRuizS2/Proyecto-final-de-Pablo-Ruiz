from django.urls import path, re_path


from .views import *
from django.conf import settings



urlpatterns = [
    #URL DE PERFILESAPP
    path('', inicio, name="inicio"),
    path('about/', about, name="about"),


    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('formulario_avatar/', crear_avatar, name="crear_avatar"),
    path('editar_avatar/', editar_avatar, name="editar_avatar"),


    path('socios/', socios, name="socios"),  
    path('formulario_socio/', crear_socio, name="crear_socio"),
    path('eliminar_socio/<socio_id>', eliminar_socio, name="eliminar_socio"),
    path('editar_socio/<socio_id>', editar_socio, name="editar_socio"),

    path('cro/', cro, name="cro"), 

    path('nosotros/', nosotros, name="nosotros"),
    path('profesores/', profesores, name="profesores"),
    path('formulario_profe/', crear_profesor, name="crear_profesor"),
    path('eliminar_profesor/<profesor_id>', eliminar_profesor, name="eliminar_profesor"),
    path('editar_profesor/<profesor_id>', editar_profesor, name="editar_profesor"),

    path('tienda/', tienda, name="tienda"),
    
    path('cursos/', cursos, name="cursos"),
    path('formulario_curso/', crear_curso, name="crear_curso"),

    path('objetos/', objetos, name="objetos"),
    path('formulario_objeto/', crear_objeto, name="crear_objeto"),

    path('municipal/', municipal, name="municipal"),

    path('eliminar_curso/<curso_id>', eliminar_curso, name="eliminar_curso"),
    path('editar_curso/<curso_id>', editar_curso, name="editar_curso"),
    path('eliminar_objeto/<objeto_id>', eliminar_objeto, name="eliminar_objeto"),
    path('editar_objeto/<objeto_id>', editar_objeto, name="editar_objeto"),

    path('blog/', blog, name="blog"),
    path('formulario_blog', crear_blog, name="crear_blog"),
    path('eliminar_blog/<blog_id>', eliminar_blog, name="eliminar_blog"),
    path('editar_blog/<blog_id>', editar_blog, name="editar_blog"),
    path('blog_detail/<blog_id>', blog_detail, name='blog_detail'),

]

