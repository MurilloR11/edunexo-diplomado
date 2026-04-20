# Edunexo - Landing + Asistente IA

Aplicación web desarrollada con **Flask** para presentar la plataforma académica **Edunexo** e integrar un **chat con GPT4All**.  
El sitio comunica propuesta de valor, misión/visión, objetivos y stack tecnológico, y además incluye una vista de asistencia IA con respuestas en tiempo real.

## ¿Qué trata el proyecto?

Edunexo es una propuesta de plataforma para gestión educativa que conecta:

- Docentes
- Estudiantes
- Acudientes
- Administradores

La solución está orientada a mostrar el producto, su impacto, su enfoque tecnológico y brindar soporte conversacional con IA local.

## Tecnologías y librerías

- **Python + Flask** (servidor web y render de plantilla)
- **GPT4All** (asistente IA local con modelo Llama 3)
- **HTML5 + CSS3**
- **JavaScript vanilla** (sin frameworks)
- **Google Fonts**:
  - Montserrat
  - Roboto
  - Syne

## Componentes principales

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
   - Card unificada con tecnologías y lenguajes
   - Logos de stack (Devicon SVG)

7. **Asistente IA**
   - Vista de chat en `/chat`, `/ai` y `/AI`
   - Integración frontend con `POST /api/chat`
   - Respuesta generada con GPT4All (modelo Llama 3)

8. **Footer**
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
- **Iconos generales**: SVG inline dentro de la plantilla
- **Logos de tecnologías/lenguajes**: SVG remotos de **Devicon** (CDN jsdelivr)

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

## Asistente IA

Chat conectado a GPT4All con modelo **Meta-Llama-3-8B-Instruct.Q4_0.gguf**.

- Ruta directa: `http://127.0.0.1:5000/chat`
- Alias: `http://127.0.0.1:5000/ai` (también `/AI`)
- Endpoint API: `POST /api/chat`
- Prompt de sistema: respuestas en español, breves y enfocadas en contexto educativo
- Longitud máxima de entrada en UI: `500` caracteres

Ejemplo de consumo del endpoint:

```bash
curl -X POST http://127.0.0.1:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Como mejorar el seguimiento de asistencia?\"}"
```

## Estado actual

Landing institucional moderna + módulo de chat IA funcional con GPT4All para asistencia local en tiempo real.
