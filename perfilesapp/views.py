from re import L
from django.shortcuts import render, redirect
from perfilesapp.models import *
from perfilesapp.forms import *
from .models import *
from .forms import *
from django.db.models import Q 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def inicio(request):
    if request.user.is_authenticated: 
        try:
            avatar= Avatar.objects.get(usuario=request.user)
            url= avatar.imagen.url
        except:
            url= "/media/avatar/generic.png" 
        return render(request, "perfilesapp/inicio.html", {"url":url} ) 


    return render(request, "perfilesapp/inicio.html") 

def about(request):
    if request.user.is_authenticated: 
        try:
            avatar= Avatar.objects.get(usuario=request.user)
            url= avatar.imagen.url
        except:
            url= "/media/avatar/generic.png" 
        return render(request, "perfilesapp/about.html", {"url":url}) 
    return render(request, "perfilesapp/about.html") 


def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
            
    form = AuthenticationForm()
    
    return render(request, "perfilesapp/login.html", {"form":form})

def register_request(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('pasword1')
            
            form.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
    
        return render(request, "perfilesapp/register.html", {"form":form})
    
    form = UserRegisterForm()
    
    return render(request, "perfilesapp/register.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")


@login_required
def editar_perfil(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    user=request.user

    if request.method == "POST":      
        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email= info["email"]
            user.first_name= info["first_name"]
            user.last_name= info["last_name"]
            user.password1= info["password1"]
            user.password2= info["password1"]

            user.save()

            return redirect("inicio")

        return render(request, "perfilesapp/editar_perfil.html", {"form":form, "url":url})

    else:
        form = UserEditForm(initial= {"email":user.email, "first_name":user.first_name, "last_name":user.last_name} )


    return render(request, "perfilesapp/editar_perfil.html", {"form":form, "url":url} )

@login_required
def crear_avatar(request):

    if request.method == "POST":
        form= AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            info_avatar=form.cleaned_data
            avatar= Avatar()
            avatar.usuario = request.user
            avatar.imagen = info_avatar["imagen"]
            avatar.save()
            return redirect("inicio")
    else:
            form= AvatarForm()
        
    return render(request, "perfilesapp/formulario_avatar.html", {"form": form})

@login_required
def editar_avatar(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    avatar = Avatar.objects.get(usuario=request.user)
    
    if request.method == "POST":
    
        formulario = AvatarForm(request.POST, request.FILES or None)
        if formulario.is_valid():
            
            info_avatar = formulario.cleaned_data

            if request.FILES:
                
                avatar.imagen = info_avatar["imagen"]
            avatar.save()
            return redirect ("editar_perfil")
    
     #get
    formulario_vacio = AvatarForm(initial={
            "imagen":avatar.imagen
            })
    

    return render(request, "perfilesapp/editar_avatar.html", {"form":formulario_vacio, "url":url}) 


def socios(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            socios = Socios.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search)).values()
            return render(request,"perfilesapp/socios.html", {"socios": socios, "search":True, "busqueda":search, "url":url})

    socios = Socios.objects.all()
    return render(request, "perfilesapp/socios.html", {"socios": socios, "url":url} )

def tienda(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    tiendaactividades = TiendaActividad.objects.all()
    tiendaobjetos = TiendaObjetos.objects.all()
    return render(request, "perfilesapp/tienda.html", {"tiendaactividades": tiendaactividades, "tiendaobjetos": tiendaobjetos, "url":url})

def objetos(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            tiendaobjetos = TiendaObjetos.objects.filter( Q(producto__icontains=search) )#
            return render(request,"perfilesapp/objetos.html", {"tiendaobjetos": tiendaobjetos, "search":True, "busqueda":search, "url":url})


    tiendaobjetos = TiendaObjetos.objects.all()
    return render(request, "perfilesapp/objetos.html", {"tiendaobjetos": tiendaobjetos, "url":url})    

@staff_member_required
def crear_objeto(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        formulario=ObjetoFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            info_objeto=formulario.cleaned_data
            objeto= TiendaObjetos()
            objeto.producto = info_objeto["producto"]
            objeto.descripcion = info_objeto["descripcion"]
            objeto.precio = info_objeto["precio"]
            objeto.imagen = info_objeto["imagen"]
            objeto.save()
            return redirect("objetos")
        
        else:
            print("Error en el formulario")
            return redirect("crear_objeto")
    
    else:
        formulariovacio=ObjetoFormulario()
        return render(request, "perfilesapp/formulario_objeto.html", {"form":formulariovacio, "url":url})

def buscar_objeto(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":

        info_objeto = request.POST["objetos"]
        
        tiendaobjetos = TiendaObjetos.objects.filter(producto__icontains=info_objeto).values()
        

        return render(request,"perfilesapp/buscar_objeto.html",{"tiendaobjetos": tiendaobjetos, "url":url})

    else: # get y otros

        tiendaobjetos =  []  
        
        return render(request,"perfilesapp/buscar_objeto.html",{"tiendaobjetos": tiendaobjetos, "url":url})

@staff_member_required
def eliminar_objeto(request, objeto_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    objetos = TiendaObjetos.objects.get(id=objeto_id)
    objetos.delete()
    
    return redirect("objetos")

@staff_member_required
def editar_objeto(request, objeto_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    objetos = TiendaObjetos.objects.get(id=objeto_id)
    
    if request.method == "POST":
    
        formulario = ObjetoFormulario(request.POST, request.FILES or None, objeto_id)
        if formulario.is_valid():
            
            info_objeto = formulario.cleaned_data
            objetos.producto = info_objeto["producto"]
            objetos.descripcion = info_objeto["descripcion"]
            objetos.precio = info_objeto["precio"]
            
            if request.FILES:
                
                objetos.imagen = request.FILES["imagen"]
            objetos.save()
            return redirect ("objetos")
    
     #get
    formulario_vacio = ObjetoFormulario(initial={
            "producto":objetos.producto,
            "descripcion": objetos.descripcion,
            "precio": objetos.precio,
            "imagen": objetos.imagen})
    

    return render(request, "perfilesapp/editar_objeto.html", {"form":formulario_vacio, "url":url})    
        

def municipal(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    return render(request, "perfilesapp/municipal.html", {"url":url})

def cro(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    return render(request, "perfilesapp/cro.html", {"url":url})

def cursos(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            cursos = TiendaActividad.objects.filter( Q(actividad__icontains=search) | Q(profesor__icontains=search))#
            return render(request,"perfilesapp/cursos.html", {"cursos": cursos, "search":True, "busqueda":search, "url":url})


    cursos = TiendaActividad.objects.all()
    return render(request, "perfilesapp/cursos.html", {"cursos": cursos, "url":url})    

@staff_member_required
def crear_curso(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "GET":
        formulariovacio=CursoFormulario()
        return render(request, "perfilesapp/formulario_curso.html", {"form":formulariovacio, "url":url})  
    
    elif request.method == "POST":
        formulario=CursoFormulario(request.POST, request.FILES)    
        
        if formulario.is_valid():
            info_curso=formulario.cleaned_data
            
            curso= TiendaActividad(actividad=info_curso["actividad"], profesor=info_curso["profesor"], dias=info_curso["dias"], turno=info_curso["turno"], precio=info_curso["precio"], imagen=info_curso["imagen"] )
            curso.save()
            return redirect("cursos")
        else:
             return redirect("cursos")
    else:
        return render(request, "perfilesapp/formulario_cursos.html", {"url":url})


def buscar_curso(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":

        info_curso = request.POST["cursos"]
        
        tiendaactividades = TiendaActividad.objects.filter(actividad__icontains=info_curso)#sacar values
        

        return render(request,"perfilesapp/buscar_curso.html",{"tiendaactividades":tiendaactividades, "url":url})

    else: # get y otros

        tiendaactividades =  []  #Curso.objects.all()
        
        return render(request,"perfilesapp/buscar_curso.html",{"tiendaactividades":tiendaactividades, "url":url})

@staff_member_required  
def eliminar_curso(request, curso_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    cursos = TiendaActividad.objects.get(id=curso_id)
    cursos.delete()
    
    return redirect("cursos")

@staff_member_required
def editar_curso(request, curso_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    cursos = TiendaActividad.objects.get(id=curso_id)
    
    if request.method == "POST":
    
        formulario = CursoFormulario(request.POST, request.FILES or None, curso_id)
        if formulario.is_valid():

            info_curso = formulario.cleaned_data
            cursos.actividad = info_curso["actividad"]
            cursos.profesor = info_curso["profesor"]
            cursos.dias = info_curso["dias"]
            cursos.turno = info_curso["turno"]
            cursos.precio = info_curso["precio"]
                
            if request.FILES:
                cursos.imagen = request.FILES["imagen"]
            cursos.save()
            return redirect ("cursos")

    
    #get
    formulario_vacio = CursoFormulario(initial={"actividad":cursos.actividad,
                                              "profesor":cursos.profesor,
                                              "dias": cursos.dias,
                                              "turno":cursos.turno,
                                              "precio":cursos.precio,
                                              "imagen": cursos.imagen})
   
    return render(request, "perfilesapp/editar_curso.html", {"form":formulario_vacio, "url":url})     

def nosotros(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            profesores = Profesor.objects.filter( Q(nombreprofesor__icontains=search) | Q(apellidoprofesor__icontains=search)).values()
            return render(request,"perfilesapp/nosotros.html", {"profesores": profesores, "search":True, "busqueda":search, "url":url})


    profesores = Profesor.objects.all()
    return render(request, "perfilesapp/nosotros.html", {"profesores": profesores, "url":url})

def blog(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    blogs= Blog.objects.all()

    return render(request, "perfilesapp/blog.html", {"blogs": blogs, "url":url})



@login_required
def crear_comentario(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "GET":
        formulariovacio=ComentarioForm()
        return render(request, "perfilesapp/blog_detail.html", {"form":formulariovacio, "url":url})

    elif request.method == "POST":

        formulario=ComentarioForm(request.POST)

        if formulario.is_valid():

            info_comentario=formulario.cleaned_data
                
            comentario=Comentario(nombre=info_comentario["nombre"], comentario=info_comentario["comentario"])
            comentario.save()
            return redirect("blog_detail")
        else:
             return redirect("blog")
        
    else:
        return render(request, "perfilesapp/blog_detail.html", {"url":url})


@staff_member_required
def crear_blog(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "GET":
        formulariovacio=BlogForm()
        return render(request, "perfilesapp/formulario_blog.html", {"form":formulariovacio, "url":url})

    elif request.method == "POST":

        formulario=BlogForm(request.POST, request.FILES)

        if formulario.is_valid():

            info_blog=formulario.cleaned_data

            blog=Blog(titulo=info_blog["titulo"], 
                      subtitulo=info_blog["subtitulo"], 
                      texto=info_blog["texto"], 
                      imagen=info_blog["imagen"], 
                      user=request.user, 
                      fecha=info_blog["fecha"])
            blog.save()
            return redirect("blog")
        else:
             return redirect("blog")
        
    else:
        return render(request, "perfilesapp/formulario_blog.html", {"url":url})

@staff_member_required 
def eliminar_blog(request, blog_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    
    return redirect("blog")

@staff_member_required
def editar_blog(request, blog_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    blog = Blog.objects.get(id=blog_id)
    
    if request.method == "POST":
    
        formulario = BlogForm(request.POST, request.FILES or None, blog_id)
        
        if formulario.is_valid():
            
            info_blog = formulario.cleaned_data
            blog.titulo = info_blog["titulo"]
            blog.subtitulo = info_blog["subtitulo"]
            blog.texto = info_blog["texto"]
            blog.fecha = info_blog["fecha"]
            
            if request.FILES:
                blog.imagen = request.FILES["imagen"]
            blog.save()  
            return redirect ("blog")
        
    
    #get
    formulario_vacio = BlogForm(initial={"titulo":blog.titulo, 
                                              "subtitulo":blog.subtitulo,
                                              "texto":blog.texto,
                                              "imagen": blog.imagen,
                                              "user":blog.user,
                                              "fecha":blog.fecha,
                                              })
    
    return render(request, "perfilesapp/editar_blog.html", {"form":formulario_vacio, "blog_post": blog, "url":url}) 
 
def blog_detail(request, blog_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    blog = Blog.objects.get(id=blog_id)   
    comentarios=Comentario.objects.filter(blog_id=blog_id)

    if request.method == "GET":
        formulariovacio=ComentarioForm()
        return render(request, "perfilesapp/blog_detail.html", {"form":formulariovacio, "blog": blog, "comentarios":comentarios, "url":url})

    elif request.method == "POST":

        formulario=ComentarioForm(request.POST)

        if formulario.is_valid():

            info_comentario=formulario.cleaned_data

            comentarios=Comentario(blog=blog, nombre=info_comentario["nombre"], comentario=info_comentario["comentario"])
            comentarios.save()
            return redirect("blog")
        else:
             return redirect("blog_detail", blog_id=blog_id)

    return render(request, "perfilesapp/blog_detail.html", {"blog": blog, "comentarios":comentarios, "url":url})


def profesores(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            profesores = Profesor.objects.filter( Q(nombreprofesor__icontains=search) | Q(apellidoprofesor__icontains=search)).values()
            return render(request,"perfilesapp/profesores.html", {"profesores": profesores, "search":True, "busqueda":search, "url":url})


    profesores = Profesor.objects.all()
    return render(request, "perfilesapp/profesores.html", {"profesores": profesores, "url":url} )


@staff_member_required
def crear_profesor(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "GET":
        formulariovacio=ProfesorFormulario()
        return render(request, "perfilesapp/formulario_profe.html", {"form":formulariovacio, "url":url})

    elif request.method == "POST":

        formulario=ProfesorFormulario(request.POST)

        if formulario.is_valid():

            info_profe=formulario.cleaned_data

            profesores=Profesor(nombreprofesor=info_profe["nombreprofesor"], apellidoprofesor=info_profe["apellidoprofesor"], edadprofesor=info_profe["edadprofesor"], emailprofesor=info_profe["emailprofesor"])
            profesores.save()
            return redirect("profesores")
        else:
             return redirect("profesores")
        
    else:
        return render(request, "perfilesapp/formulario_profe.html", {"url":url})

def buscar_profesor(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            profesor = Profesor.objects.filter( Q(nombreprofesor__icontains=search) | Q(apellidoprofesor__icontains=search)).values()
            return render(request,"perfilesapp/profesores.html", {"profesor": profesor, "search":True, "busqueda":search, "url":url})

    profesor = Profesor.objects.all()
    return render(request, "perfilesapp/profesores.html", {"profesor": profesor, "url":url} )

@staff_member_required 
def eliminar_profesor(request, profesor_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    profesor = Profesor.objects.get(id=profesor_id)
    profesor.delete()
    
    return redirect("profesores")

@staff_member_required
def editar_profesor(request, profesor_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    profesor = Profesor.objects.get(id=profesor_id)
    
    if request.method == "POST":
    
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            info_profesor = formulario.cleaned_data
            profesor.nombreprofesor = info_profesor["nombreprofesor"]
            profesor.apellidoprofesor = info_profesor["apellidoprofesor"]
            profesor.edadprofesor = info_profesor["edadprofesor"]
            profesor.emailprofesor = info_profesor["emailprofesor"]
            profesor.save()
        
            return redirect ("profesores")
        
    
    #get
    formulario_vacio = ProfesorFormulario(initial={"nombreprofesor":profesor.nombreprofesor,
                                              "apellidoprofesor":profesor.apellidoprofesor,
                                              "edadprofesor": profesor.edadprofesor,
                                              "emailprofesor":profesor.emailprofesor})
    
    return render(request, "perfilesapp/editar_profesor.html", {"form":formulario_vacio, "url":url})    
 
 
@staff_member_required     
def crear_socio(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "GET":
        formulariovacio=SocioFormulario()
        return render(request, "perfilesapp/formulario_socio.html", {"form":formulariovacio, "url":url})  
    
    elif request.method == "POST":
        formulario=SocioFormulario(request.POST)    
        
        if formulario.is_valid():
            info_socio=formulario.cleaned_data
            
            socio= Socios(nombre=info_socio["nombre"], apellido=info_socio["apellido"], edad=info_socio["edad"], fechanacimiento=info_socio["fechanacimiento"], email=info_socio["email"] )
            socio.save()
            return redirect("socios")
        else:
             return redirect("socios")
    else:
        return render(request, "perfilesapp/formulario_socio.html", {"url":url})

@login_required
def buscar_socio(request):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    if request.method == "POST":

        info_socio = request.POST["socios"]
        
        socio = Socios.objects.filter(nombre=info_socio).values()
        

        return render(request,"perfilesapp/buscar_socio.html",{"socios":socio, "url":url})

    else: # get y otros

        socio =  []  #Curso.objects.all()
        
        return render(request,"perfilesapp/buscar_socio.html", {"socios":socio, "url":url})

@staff_member_required
def eliminar_socio(request, socio_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    socios = Socios.objects.get(id=socio_id)
    socios.delete()
    
    return redirect("socios")

@staff_member_required
def editar_socio(request, socio_id):
    try:
        avatar= Avatar.objects.get(usuario=request.user)
        url= avatar.imagen.url
    except:
        url= "/media/avatar/generic.png" 

    socio = Socios.objects.get(id=socio_id)
    
    if request.method == "POST":
    
        formulario = SocioFormulario(request.POST)
        if formulario.is_valid():
            info_socio = formulario.cleaned_data
            socio.nombre = info_socio["nombre"]
            socio.apellido = info_socio["apellido"]
            socio.edad = info_socio["edad"]
            socio.email = info_socio["email"]
            socio.fechanacimiento = info_socio["fechanacimiento"]
            socio.save()
        
            return redirect ("socios")
        
    
    #get
    formulario_vacio = SocioFormulario(initial={"nombre":socio.nombre,
                                              "apellido":socio.apellido,
                                              "edad": socio.edad,
                                              "email":socio.email,
                                              "fechanacimiento":socio.fechanacimiento})
    
    return render(request, "perfilesapp/editar_socio.html", {"form":formulario_vacio, "url":url})    
        

 



  

