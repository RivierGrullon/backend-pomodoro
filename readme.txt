BACKEND-POMODORO
================
api codificada con python, flask y mongodb para servir de backend a una aplicacion para administar pomodoros

PRINCIPIO
=========
usted es un usuario que desea registrarse, logearse y acceder al dashboard de la aplicacion, entonces
siga los siguientes pasos:
-para registrarse debe enviar una solicitud POST a (por ahora) la ruta: http://localhost:5000/users
con el siguiente json:
{"name": "su nombre", "email": "su email", "username": "su nombre de usuario", "password": "su clave"}
-para visualizar los usuarios registrados debe enviar una solicitud GET a la ruta: http://localhost:5000/users
-para hacer login enviar una solicitud POST a la ruta: http://localhost:5000/login_user
con el siguiente json: {"username": "su nombre de usuario", "password": "su clave"}
-para desloguearse enviar una solicitud POST a la ruta: http://localhost:5000/logout
para enviar estas solicitudes debe usar una herramienta de testing api como postman o insomnia

INSTALACION
===========
1- asegurese tener instalado mongo, python, pip
2- dirijase a la carpeta donde descargara el proyecto
3- clone el repositorio dentro de esta carpeta
4- entre en backend-pomodoro (> cd backend-pomodoro)
5- instale virtual env (> pip install virtualenv)
6- declare el entorno virtual (> virtualenv venv)
7- active el entorno virtual (> .\venv\Scripts\activate)
8- instale las dependencias (> pip install -r requirements.txt)
9- corra mongo en un terminal individual (> mongod)
10- corra el servidor (> python src/app.py)
11- probar las rutas con postman o insomnia