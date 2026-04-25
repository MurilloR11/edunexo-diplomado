# Edunexo - Landing + Asistente IA

Aplicación web desarrollada con **Flask** para presentar la plataforma académica **Edunexo**, gestionar autenticación básica de usuarios y ofrecer un chat local con **GPT4All**.

## ¿Qué trata el proyecto?

Edunexo es una propuesta de plataforma para gestión educativa orientada a docentes, estudiantes, acudientes y administradores. El proyecto incluye landing institucional, formularios de registro e inicio de sesión, dashboard temporal y asistente IA con respuestas en español.

## Tecnologías y librerías

- **Python + Flask**: servidor web, rutas y render de plantillas.
- **Flask-SQLAlchemy**: modelos y conexión a MySQL.
- **Flask-Migrate / Alembic**: migraciones de base de datos.
- **PyMySQL**: driver para conectar Flask con MySQL.
- **Werkzeug**: hash y validación de contraseñas.
- **GPT4All**: asistente IA local con modelo Llama 3.
- **HTML5, CSS3 y JavaScript vanilla**.
- **Phosphor Icons, Google Fonts y Devicon** desde CDN.

## Componentes principales

1. **Landing page**: vista principal en `/` con secciones institucionales, stack tecnológico y CTAs.
2. **Autenticación**: registro en `/register`, inicio de sesión en `/login` y cierre en `/logout`.
3. **Dashboard temporal**: vista protegida en `/dashboard`, con sidebar, perfil, navegación y resumen visual.
4. **Asistente IA**: vistas `/chat`, `/ai` y `/AI`, con endpoint `POST /api/chat`.
5. **Base de datos**: tabla `users` gestionada por migraciones en MySQL.

## Estructura del proyecto

```text
edunexo-diplomado/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── models/
│   ├── __init__.py
│   └── user.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   └── versions/
│       └── 001_create_users.py
├── templates/
│   ├── index.html
│   ├── chat.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/
│   ├── index.css
│   ├── adunexo.logo.svg
│   ├── css/
│   │   ├── chat.css
│   │   ├── login.css
│   │   ├── register.css
│   │   └── dashboard.css
│   └── js/
└── .gitignore
```

## Configuración

La configuración principal está en `config.py`.

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/edunexo"
```

Puedes sobrescribirla con variables de entorno:

```bash
export DATABASE_URL="mysql+pymysql://usuario:clave@localhost/edunexo"
export SECRET_KEY="clave-segura-para-sesiones"
```

El proyecto está planteado para **MySQL**, no SQLite.

## Cómo ejecutar el proyecto

1. Crear y activar entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear la base de datos MySQL si aún no existe:

```bash
mysql -u root -e "CREATE DATABASE IF NOT EXISTS edunexo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

4. Aplicar migraciones:

```bash
flask --app app.py db upgrade
```

5. Ejecutar la app:

```bash
python3 app.py
```

6. Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Migraciones

Las migraciones ya están inicializadas en `migrations/`. No ejecutes `flask db init` otra vez.

```bash
flask --app app.py db migrate -m "descripcion del cambio"
flask --app app.py db upgrade
flask --app app.py db downgrade
flask --app app.py db current
flask --app app.py db history
```

## Autenticación

El modelo `User` está en `models/user.py` y usa la tabla `users`. Las contraseñas se guardan como hash con Werkzeug. Si un usuario ya inició sesión, `/login` y `/register` redirigen a `/dashboard`. Si no hay sesión activa, `/dashboard` redirige a `/login`.

## Asistente IA

Chat conectado a GPT4All con modelo **Meta-Llama-3-8B-Instruct.Q4_0.gguf**.

- Ruta directa: `http://127.0.0.1:5000/chat`
- Alias: `http://127.0.0.1:5000/ai` y `/AI`
- Endpoint API: `POST /api/chat`
- Prompt de sistema: respuestas breves, en español y enfocadas en contexto educativo.

Ejemplo:

```bash
curl -X POST http://127.0.0.1:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Como mejorar el seguimiento de asistencia?\"}"
```

## Estado actual

Landing institucional, autenticación con MySQL, dashboard temporal protegido y asistente IA local con GPT4All.
