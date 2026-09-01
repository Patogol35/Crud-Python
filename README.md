Sistema de Gestión de Productos

Aplicación web para la gestión de productos mediante una interfaz moderna desarrollada con React y Material UI, conectada a un backend desarrollado con Python y Flask.

El sistema permite realizar operaciones CRUD completas sobre los productos: crear, consultar, actualizar y eliminar.

🚀 Tecnologías utilizadas
Frontend
React
Vite
Material UI (MUI)
JavaScript
CSS
Backend
Python
Flask
Flask-CORS
API REST
Base de datos
SQLite
✨ Funcionalidades
📋 Listar productos
➕ Crear productos
✏️ Editar productos
🗑️ Eliminar productos
🔄 Actualizar listado
🔔 Notificaciones mediante Snackbar

⚙️ Instalación
1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
2. Entrar al proyecto
cd TU-REPOSITORIO
🐍 Configuración del Backend

Entrar a la carpeta del backend:

cd backend

Crear un entorno virtual:

python -m venv venv

Activar el entorno virtual en Windows:

venv\Scripts\activate

Instalar las dependencias:

pip install flask flask-cors

Ejecutar Flask:

python app.py

El backend estará disponible en:

http://127.0.0.1:5000
⚛️ Configuración del Frontend

En otra terminal, entrar al frontend:

cd frontend

Instalar las dependencias:

npm install

Ejecutar el proyecto:

npm run dev

La aplicación estará disponible normalmente en:

http://localhost:5173
🔗 Comunicación Frontend → Backend

El frontend se comunica con Flask mediante fetch() y una API REST.

Ejemplo:

React
  ↓
fetch()
  ↓
Flask API
  ↓
SQLite

URL del backend en desarrollo:

http://127.0.0.1:5000
📌 Endpoints principales
Método	Endpoint	Descripción
GET	/	Verificar API
GET	/productos	Obtener productos
GET	/productos/<id>	Obtener un producto
POST	/productos	Crear producto
PUT	/productos/<id>	Actualizar producto
DELETE	/productos/<id>	Eliminar producto
📦 Ejemplo de producto
{
  "nombre": "Laptop",
  "descripcion": "Laptop para trabajo y desarrollo",
  "precio": 850,
  "categoria": "Tecnología"
}
🔐 Variables de entorno

Si el proyecto utiliza variables de entorno, crea un archivo .env y no lo subas a GitHub.

Ejemplo:

VITE_API_URL=http://127.0.0.1:5000

En producción se debe configurar la URL correspondiente al backend desplegado.

🌐 Producción

La arquitectura del proyecto puede desplegarse de la siguiente manera:

Frontend
React + Vite
     ↓
  Vercel
     ↓
Backend
Python + Flask
     ↓
Base de datos
🎯 Objetivo del proyecto

Este proyecto fue desarrollado como una aplicación práctica para demostrar la integración entre un frontend moderno en React y un backend REST desarrollado con Python y Flask, implementando operaciones CRUD y una interfaz responsive.

👨‍💻 Autor

Jorge Patricio Santamaría

Desarrollador de Software

⭐ Si este proyecto te resulta útil, puedes darle una estrella al repositorio.
📱 Diseño responsive
🎨 Interfaz desarrollada con Material UI
🔗 Comunicación entre React y Flask mediante API REST
