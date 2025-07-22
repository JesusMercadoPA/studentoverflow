# StudentOverflow

**StudentOverflow** es una plataforma de preguntas y respuestas inspirada en StackOverflow, diseñada para estudiantes.  
Permite que los usuarios se registren, inicien sesión, publiquen preguntas y respondan las de otros usuarios.

---

## 🚀 Tecnologías utilizadas

- **[Reflex](https://reflex.dev/)** – Framework web en Python.
- **[Supabase](https://supabase.com/)** – Base de datos y autenticación.
- **[JWT (JSON Web Tokens)](https://jwt.io/)** – Para autenticación y autorización segura.
- **Python 3.11+**

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU-USUARIO/studentoverflow.git
cd studentoverflow

2. Crear entorno virtual e instalar dependencias
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto con las claves de tu proyecto Supabase y la clave secreta para JWT:

ini
Copiar
Editar
SUPABASE_URL=tu_url
SUPABASE_KEY=tu_api_key
JWT_SECRET=clave_secreta
4. Ejecutar la aplicación
bash
Copiar
Editar
reflex run
📂 Estructura de carpetas
csharp
Copiar
Editar
studentoverflow/
│
├── components/        # Componentes de interfaz (botones, layouts)
├── models/            # Modelos de datos (Preguntas, Respuestas, Usuarios)
├── pages/             # Páginas de la aplicación (home, login, signup)
├── static/            # Archivos estáticos
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación principal
✨ Funcionalidades
Registro e inicio de sesión con autenticación JWT.

Persistencia de sesión.

Publicación y respuesta a preguntas.

Interfaz dinámica basada en el estado de sesión del usuario.

📜 Licencia
Este proyecto está bajo la licencia MIT.

🔗 Enlace del repositorio
https://github.com/TU-USUARIO/studentoverflow

