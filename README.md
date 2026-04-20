# Edunexo - Landing Page Institucional

Landing page desarrollada con **Flask** para presentar la plataforma académica **Edunexo**.  
El sitio comunica propuesta de valor, misión/visión, objetivos y stack tecnológico, con diseño moderno, animaciones y comportamiento responsivo.

## ¿Qué trata el proyecto?

Edunexo es una propuesta de plataforma para gestión educativa que conecta:

- Docentes
- Estudiantes
- Acudientes
- Administradores

La homepage está orientada a mostrar el producto, su impacto y su enfoque tecnológico.

## Tecnologías y librerías

- **Python + Flask** (servidor web y render de plantilla)
- **GPT4All** (asistente IA local con modelo Llama 3)
- **HTML5 + CSS3**
- **JavaScript vanilla** (sin frameworks)
- **Google Fonts**:
  - Montserrat
  - Roboto
  - Syne

## Componentes principales de la homepage

1. **Header/Navbar**
   - Logo clickeable al inicio
   - Navegación por anclas
   - CTA "Registrate"
   - Menú hamburguesa en móvil

2. **Hero**
   - Título y subtítulo principal
   - CTAs
   - Métricas destacadas (contador animado)
   - Visual con cards flotantes (en desktop/tablet)

3. **Sección Nosotros**
   - Presentación de la propuesta
   - Cards de funcionalidades clave

4. **Misión y Visión**
   - 2 cards principales con puntos estratégicos

5. **Objetivos**
   - Objetivo general
   - Objetivos específicos en cards

6. **Tecnologías**
   - Cards de Flask y MySQL

7. **Footer**
   - Marca
   - Redes sociales
   - Enlaces de navegación/roles/legal

## Animaciones e interacciones

- Animaciones al hacer scroll entre secciones (IntersectionObserver)
- Contador animado en los números del hero
- Respeto por accesibilidad con `prefers-reduced-motion`
- Menú móvil con apertura/cierre y comportamiento adaptable al resize

## Diseño responsivo

Se aplican breakpoints para adaptar layout en distintos dispositivos:

- `1200px`
- `1024px`
- `900px`
- `600px`

En móvil se simplifica la experiencia visual para evitar saturación (por ejemplo, ocultando ciertos bloques de imagen en pantallas pequeñas).

## Origen de imágenes y recursos visuales

- **Logo**: archivo local `static/adunexo.logo.svg`
- **Imágenes de contenido**: URLs remotas de **Unsplash** (`images.unsplash.com`)
- **Iconos**: SVG inline dentro de la plantilla (sin librería externa de iconos)

## Estructura del proyecto

```text
edunexo-diplomado/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── chat.html
├── static/
│   ├── index.css
│   ├── css/chat.css
│   └── adunexo.logo.svg
└── .gitignore
```

## Cómo ejecutar el proyecto

1. Crear y activar entorno virtual (opcional pero recomendado).
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la app:

```bash
python app.py
```

4. Abrir en navegador:

```text
http://127.0.0.1:5000
```

## Estado actual

Landing page institucional con UI moderna, responsive y animaciones. Vista de chat con integración a GPT4All para asistencia IA local.

## Asistente IA

Chat conectado a GPT4All con modelo **Meta-Llama-3-8B-Instruct.Q4_0.gguf**.

- Ruta directa: `http://127.0.0.1:5000/chat`
- Alias: `http://127.0.0.1:5000/ai` (también `/AI`)
- Endpoint API: `POST /api/chat`
