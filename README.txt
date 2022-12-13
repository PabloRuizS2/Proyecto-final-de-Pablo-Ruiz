#NOMBRE
Proyecto Club de Kayaks y Canoas de Tigre
#Creador
Pablo Ariel Ruiz Segura
#DESCRIPCION Y ESTADO DEL PROYECTO
Plataforma conjunta de blog + e-commerce, en donde se brinda acceso tanto a socios, instructores y administradores para poder
ver y cargar data a la web.
Se encuentra en proceso, ya que resulta de un trabajo academico realizado para curso de Python de Coderhouse.
Se debe mejorar:
- [ ]Interfaz
- [ ]Agregar messages pop up
- [ ]Activar y dar funcionalidad al bloque de "contacto" ubicado en el pie de la web
- [ ]Continuar la compra con carrito de compra
- [ ]Agregar insignias "me gusta" a los posteos de blog
- [ ]Mejorar el login/agregado de avatars
- [ ]Correrlo en servidor
- [ ]Corregir Comentarios en posteos de blog
- [ ]Colocar fecha y usuario automaticamente en la creacion del posteo del blog

#INSIGNIA
Se encuentra en estado Betha, si bien necesita mejoras, puede ser testeado por usuarios.

#INSTALACION

*Instalar Python 3.10
*Instalar Visual Code
*Instalar Db Browser
*Instalar SQLite3
*Instalar Pillow
*Descargar Repositorio "Proyecto-final-pablo-coderhouse"
*Abrir con Visual Code:
*- Correr nuestro programa: 
*python .\manage.py makemigrations
*python .\manage.py migrate
*python .\manage.py runserver

#USO QUE HACE MI PAGINA

http://127.0.0.1:8000/ - Ruta que deriva en el inicio de la web - Nav Bar interactiva, botones de inicio de sesion y registro, y banner con fotos que referencian a urls de la web. Si se es usuario admin, se activa boton para editar, agregar y eliminar Instructores

&nbsp; http://127.0.0.1:8000/formulario_profe/ - Crear un instructor

&nbsp; http://127.0.0.1:8000/editar_profesor/profe_id - Editar informacion de un instructor

http://127.0.0.1:8000/about/ - Sobre las autoras del proyecto

http://127.0.0.1:8000/nosotros/ - Informacion sobre el club y listado de Instructores en donde se puede buscar por nombre y apellido. Incluye boton que deriba en la ruta /about, con mas informacion sobre el autor.

http://127.0.0.1:8000/blog/ - Blog, acceso al blog, mediante el boton ver mas, a cada posteo

http://127.0.0.1:8000/blog_detail/id - Posteo con detalles.

http://127.0.0.1:8000/tienda/ - Tienda, crea acceso a los dos tipos de tienda mediante botones:

&nbsp; http://127.0.0.1:8000/cursos/ - Nuestros cursos, lista mediante cards. Si se es socio admin, tiene funcionalidades de crear, editr y eliminar cursos.Acceso mediante botona a "volver a tienda"

&nbsp; http://127.0.0.1:8000/objetos/ - Nuestros Productos, lista mediante cards. Si se es socio admin, tiene funcionalidades de crear, editr y eliminar cursos.Acceso mediante botona a "volver a tienda"

http://127.0.0.1:8000/municipal/ - Informacion sobre la escuela municipal de Kayak

http://127.0.0.1:8000/cro/ - Informacion sobre Club de Kayaks y Canoas de Tigre

http://127.0.0.1:8000/login/ - Formulario para realizar el login

http://127.0.0.1:8000/register/ - Formulario de Registro

#link de video de muestra de como funciona la pagina
https://drive.google.com/drive/folders/1MzJQPXyJC7aznphYquYVLbRpsmYHM5ZY?usp=sharing

     
