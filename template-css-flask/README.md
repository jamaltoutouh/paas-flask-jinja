# Flask con Templates y CSS - Ejemplo Básico

Este es un ejemplo simple de una aplicación Flask que demuestra el uso de **templates con herencia** y **archivos CSS estáticos**.

## 📁 Estructura del Proyecto

```
template-css-flask/
├── app.py                 # Aplicación Flask principal
├── static/               # Archivos estáticos (CSS, imágenes, JS)
│   └── css/
│       └── style.css     # Estilos CSS básicos
├── templates/            # Plantillas HTML con Jinja2
│   ├── base.html         # Plantilla base para herencia
│   └── index.html        # Página principal
└── README.md             # Este archivo
```

## 🚀 Funcionalidades Implementadas

### 1. **Aplicación Flask Simple** (`app.py`)
- Una sola ruta: página de inicio (`/`)
- Uso de `render_template()` para renderizar plantillas HTML
- Paso de variables desde Python a los templates

### 2. **System de Templates con Jinja2**
- **`base.html`**: Plantilla base con estructura HTML común
- **`index.html`**: Plantilla hija que extiende `base.html`
- **Herencia de templates**: `{% extends "base.html" %}`
- **Bloques de contenido**: `{% block contenido %}...{% endblock %}`

### 3. **CSS Estático**
- Archivo CSS básico que cambia la tipografía a Georgia
- Contenedor centrado con sombra sutil
- Enlazado usando `url_for('static', filename='css/style.css')`

## 💻 Cómo Ejecutar

### Prerrequisitos
```bash
# Instalar Flask (si no está instalado)
pip3 install flask
```

### Ejecutar la Aplicación
```bash
# Navegar al directorio del proyecto
cd template-css-flask

# Ejecutar la aplicación
python3 app.py
```

### Acceder a la Aplicación
- Abrir el navegador y ir a: `http://127.0.0.1:5000/`
- La aplicación se ejecuta en modo debug (recarga automática)

## 🔧 Código Explicado

### app.py - Aplicación Principal
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_template() busca archivos en la carpeta 'templates/'
    return render_template('index.html', 
                         titulo="Mi App Flask",
                         mensaje="¡Hola, mundo con templates!")
```

### base.html - Plantilla Base
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <title>{% block titulo %}Mi App Flask{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        {% block contenido %}
        {% endblock %}
    </div>
</body>
</html>
```

### index.html - Plantilla Hija
```html
{% extends "base.html" %}

{% block titulo %}{{ titulo }}{% endblock %}

{% block contenido %}
    <h1>{{ titulo }}</h1>
    <p>{{ mensaje }}</p>
{% endblock %}
```

## 🔗 Proceso Detallado de Herencia de Templates

### ¿Cómo se renderiza `index.html` desde `base.html`?

Cuando Flask ejecuta `render_template('index.html', ...)`, Jinja2 realiza el siguiente proceso paso a paso:

#### **Paso 1: Lectura del Template Hijo (`index.html`)**
```html
<!-- index.html -->
{% extends "base.html" %}           ← Jinja2 detecta la herencia
{% block titulo %}{{ titulo }}{% endblock %}
{% block contenido %}
    <h1>{{ titulo }}</h1>
    <p>{{ mensaje }}</p>
    <p>Esta es una aplicación Flask simple...</p>
{% endblock %}
```

#### **Paso 2: Carga del Template Padre (`base.html`)**
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>{% block titulo %}Mi App Flask{% endblock %}</title>  ← Bloque definido
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        {% block contenido %}{% endblock %}                     ← Bloque vacío
    </div>
</body>
</html>
```

#### **Paso 3: Fusión de Templates**
Jinja2 **reemplaza** los bloques del padre con los del hijo:

```html
<!-- Resultado ANTES de sustituir variables -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>{{ titulo }}</title>           ← Bloque 'titulo' de index.html
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>{{ titulo }}</h1>              ← Bloque 'contenido' de index.html
        <p>{{ mensaje }}</p>
        <p>Esta es una aplicación Flask simple...</p>
    </div>
</body>
</html>
```

#### **Paso 4: Sustitución de Variables**
Con las variables pasadas desde Python: `titulo="Mi App Flask"`, `mensaje="¡Hola, mundo con templates!"`

```html
<!-- HTML FINAL enviado al navegador -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Mi App Flask</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Mi App Flask</h1>
        <p>¡Hola, mundo con templates!</p>
        <p>Esta es una aplicación Flask simple con templates y CSS básico.</p>
    </div>
</body>
</html>
```

### 🎯 **Reglas Importantes de la Herencia**

1. **`{% extends %}` debe ser la primera línea** del template hijo
2. **Los bloques del hijo REEMPLAZAN completamente** los del padre
3. **Si un bloque no se define en el hijo**, se usa el del padre (o queda vacío)
4. **Las variables se sustituyen DESPUÉS** de la fusión de templates
5. **URL estáticas se resuelven automáticamente** con `url_for()`

### 📊 **Comparación Visual**

| Template | Bloque `titulo` | Bloque `contenido` |
|----------|-----------------|-------------------|
| **base.html** | `Mi App Flask` (por defecto) | *vacío* |
| **index.html** | `{{ titulo }}` | `<h1>{{ titulo }}</h1><p>{{ mensaje }}</p>...` |
| **Resultado** | `Mi App Flask` | Contenido completo de index.html |

## 📚 Conceptos de Jinja2 Demostrados

| Concepto | Sintaxis | Descripción |
|----------|----------|-------------|
| **Herencia de Templates** | `{% extends "base.html" %}` | Hereda estructura de otra plantilla |
| **Bloques** | `{% block nombre %}...{% endblock %}` | Define secciones reemplazables |
| **Variables** | `{{ variable }}` | Muestra valores pasados desde Python |
| **URLs estáticas** | `{{ url_for('static', filename='...') }}` | Genera URLs para archivos estáticos |

## 🎨 CSS Aplicado

El archivo `style.css` incluye estilos muy básicos:
- **Tipografía**: Cambio a fuente Georgia
- **Layout**: Contenedor centrado con sombra
- **Colores**: Fondo gris claro, contenido en blanco

## 🔄 Flujo de la Aplicación

1. **Usuario accede** → `http://127.0.0.1:5000/`
2. **Flask ejecuta** → función `home()`
3. **render_template()** → busca `index.html` en `templates/`
4. **Jinja2 procesa** → `index.html` extiende `base.html`
5. **Variables sustituidas** → `{{ titulo }}` y `{{ mensaje }}`
6. **CSS aplicado** → desde `static/css/style.css`
7. **HTML final enviado** → al navegador del usuario

## 📝 Notas Importantes

- **Carpetas obligatorias**: `templates/` y `static/` deben estar en la raíz del proyecto
- **Modo debug**: `app.run(debug=True)` permite recarga automática
- **Herencia**: Los bloques en plantillas hijas reemplazan los de la base
- **Variables**: Se pasan como argumentos a `render_template()`

## 🚧 Posibles Mejoras

Para expandir este ejemplo, podrías añadir:
- Más rutas y páginas
- Formularios HTML
- Base de datos
- Autenticación de usuarios
- CSS más avanzado (Bootstrap, etc.)
- JavaScript interactivo

---

**¡Ejemplo creado para aprender Flask de forma simple y práctica!** 🎓
