Sistema de Gestión de Productos

Aplicación web para la gestión de productos mediante una interfaz moderna desarrollada con React y Material UI, conectada a un backend desarrollado con Python y Flask.

El sistema permite realizar operaciones CRUD completas sobre los productos: crear, consultar, actualizar y eliminar.

---

🚀 Tecnologías utilizadas:

- Frontend
  
- React
  
- Vite
  
- Material UI (MUI)

- JavaScript

- CSS

Backend

- Python

- Flask

- Flask-CORS

- API REST

Base de datos

- SQLite

---

✨ Funcionalidades

- Listar productos

- Crear productos

- Editar productos

- Eliminar productos

- Actualizar listado

- Notificaciones mediante Snackbar

---

⚙️ Instalación

1. Clonar el repositorio

Backend:

```bash

git clone https://github.com/Patogol35/crud-python/

```

Frontend

```bash

git clone https://github.com/Patogol35/crud-react/

 ```

2. Configuración del Backend

Entrar a la carpeta del backend:

```bash

cd crud-python

```

Crear un entorno virtual:

```bash

python -m venv venv

```

Activar el entorno virtual en Windows:

```bash

venv\Scripts\activate

```

Instalar las dependencias:

```bash

pip install flask flask-cors

```

Ejecutar Flask:

```bash

python app.py

```

El backend estará disponible en:

http://127.0.0.1:5000


3. Configuración del Frontend

En otra terminal, entrar al frontend:

```bash

cd crud-front

```

Instalar las dependencias:

```bash

npm install

```

Ejecutar el proyecto:

```bash

npm run dev

```

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

---

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

---

🔐 Variables de entorno

Si el proyecto utiliza variables de entorno, crea un archivo .env y no lo subas a GitHub.

Ejemplo:

VITE_API_URL=http://127.0.0.1:5000

En producción se debe configurar la URL correspondiente al backend desplegado.

---

Este proyecto fue desarrollado como una aplicación práctica para demostrar la integración entre un frontend moderno en React y un backend REST desarrollado con Python y Flask, implementando operaciones CRUD y una interfaz responsive.

---

👨‍💻 Autor

Jorge Patricio Santamaría

Máster en Ingeniería de Software y Sistemas Informáticos

---

⭐ Si este proyecto te resulta útil, puedes darle una estrella al repositorio.

📱 Diseño responsive

🎨 Interfaz desarrollada con Material UI

🔗 Comunicación entre React y Flask mediante API REST
