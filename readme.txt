BACKEND-POMODORO
================
api codificada con python, flask y mongodb para servir de backend a una aplicacion para administar pomodoros

PRINCIPIO
=========
usted es un usuario que desea registrarse en la aplicacion, entonces lo primero que debe hacer es
enviar una solicitud POST a (por ahora) la ruta: http://localhost:5000/users con el siguiente json:
{"name": "su nombre", "email": "su email", "username": "su nombre de usuario", "password": "su clave"}
para visualizarlo desde la base de datos enviar una solicitud GET a la ruta: http://localhost:5000/users
mas adelante agregaremos mas funcionalidad para el manejo de usuarios, logearse y manejar los pomodoros.
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