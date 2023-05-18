# DOCUMENTACION

Primero se tiene que clonar el repositorio

~~~
git clone https://github.com/EnriqueChiu/PruebaTecnico_Django_Backend.git
~~~

Luego para ejecutar el backend se debe ingresar a la carpeta backend y abrir un terminal e instalar lo siguiente librerias

~~~
pip install Django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install firebase-admin
~~~

Ya una vez instalado las librerias necesarias se procede a correr el backend con el siguiente comando

~~~
python manage.py runserver
o
python3 manage.py runserver
~~~

Esto seria para correr el backend, por defecto el server estara en el http://127.0.0.1:8000/ o http://localhost:8000/


## Especificacion tecnicas donde se desarrollo el backend

* Windows 10
* Procesador AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx   2.00 GHz
* 8.00 GB de RAM
* Sistema operativo de 64 bits

## Tecnologia que se uso

* Python Django version 3.8.10 (Backend)
* Firebase (DB)
* Simplejwt (Generacion de token, duracion de 5min por sesion)