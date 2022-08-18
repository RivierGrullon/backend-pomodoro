BACKEND-POMODORO
================
api codificada con python, flask y mongodb para servir de backend a una aplicacion para administar tasks

PRINCIPIO
=========
usted es un usuario que desea utilizar la aplicacion de pomodoro, entonces debe registrarse, hacer login y
luego usar el token para visitar la rutas protegidas.

USO
====
lo primero que debe hacer es enviar una solicitud POST a la ruta:
http://localhost:5000/createuser con el siguiente json:
{"email": "su email", "username": "su nombre de usuario", "password": "su clave"}

para hacer login en la aplicacion en viar una solicitud POST a http://localhost:5000/login con el json
{"username": "su nombre de usuario", "password": "su clave"} y recibira un token, el cual enviara como
bearer token en la autorizacion de postman junto a la ruta deseada.

otras rutas disponibles para los usuarios son:
http://localhost:5000/getuser para visualizar los datos de su usuario,
http://localhost:5000/updatepassword para actualizar el password,
http://localhost:5000/createtask para crear una task,
http://localhost:5000/deletetask para eliminar una task,
http://localhost:5000/updatetask para actualizar una task,
http://localhost:5000/gettask para visualizar sus tasks.

para enviar estas solicitudes debe usar una herramienta de testing api como postman o insomnia

INSTALACION
===========
1- asegurese tener instalado python, pip
2- dirijase a la carpeta donde descargara el proyecto
3- clone el repositorio dentro de esta carpeta
4- entre en backend-pomodoro (> cd backend-pomodoro)
5- instale virtual env (> pip install virtualenv)
6- declare el entorno virtual (> virtualenv venv)
7- active el entorno virtual (> .\venv\Scripts\activate)
8- instale las dependencias (> pip install -r requirements.txt)
9- corra el servidor (> python src/app.py)
10- probar las rutas con postman o insomnia