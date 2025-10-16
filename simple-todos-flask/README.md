# Simple TODOs Flask - Aplicación CRUD sin Base de Datos

Una aplicación web simple para gestionar tareas (TODOs) usando **Flask** sin base de datos. Los datos se almacenan en una **lista de Python** en memoria.

## 🎯 Funcionalidades CRUD Implementadas

### ✅ **CREATE (Crear)**
- Formulario para crear nuevas tareas
- Validación de campos obligatorios
- Generación automática de ID único
- Fecha de creación automática

### 📖 **READ (Consultar)**
- Lista de todas las tareas con estadísticas
- Vista detallada de cada tarea individual
- Filtrado visual por estado (completada/pendiente)
- Contador de tareas totales y completadas

### ✏️ **UPDATE (Actualizar)**
- Formulario de edición para tareas existentes
- Cambio de estado (completada ↔ pendiente)
- Modificación de título y descripción
- Preservación del ID y fecha de creación

### 🗑️ **DELETE (Eliminar)**
- Eliminación de tareas con confirmación
- Eliminación permanente de la lista

## 📁 Estructura del Proyecto

```
simple-todos-flask/
├── app.py                    # Aplicación Flask principal con lógica CRUD
├── static/                   # Archivos estáticos
│   └── css/
│       └── style.css         # Estilos personalizados
├── templates/                # Plantillas HTML con Jinja2
│   ├── base.html            # Plantilla base con Bootstrap
│   ├── index.html           # Lista de tareas (READ)
│   ├── nueva_tarea.html     # Formulario crear (CREATE)
│   ├── editar_tarea.html    # Formulario editar (UPDATE)
│   └── detalle_tarea.html   # Vista detallada (READ individual)
└── README.md                # Este archivo
```

## 🚀 Cómo Ejecutar

### Prerrequisitos
```bash
# Asegurar que Flask está instalado
pip3 install flask
```

### Ejecutar la Aplicación
```bash
# Navegar al directorio
cd simple-todos-flask

# Ejecutar la aplicación
python3 app.py
```

### Acceder a la Aplicación
- **URL principal:** `http://127.0.0.1:5000/`
- **Crear tarea:** `http://127.0.0.1:5000/nueva`
- **Ver tarea:** `http://127.0.0.1:5000/tarea/<id>`
- **Editar tarea:** `http://127.0.0.1:5000/editar/<id>`

## 🛠️ Rutas y Funcionalidades

| Ruta | Método | Funcionalidad | Descripción |
|------|--------|---------------|-------------|
| `/` | GET | **READ** - Lista todas | Página principal con todas las tareas |
| `/nueva` | GET | **CREATE** - Formulario | Muestra formulario para nueva tarea |
| `/crear` | POST | **CREATE** - Procesar | Procesa y crea la nueva tarea |
| `/tarea/<id>` | GET | **READ** - Individual | Muestra detalles de una tarea |
| `/editar/<id>` | GET | **UPDATE** - Formulario | Muestra formulario de edición |
| `/actualizar/<id>` | POST | **UPDATE** - Procesar | Procesa y actualiza la tarea |
| `/completar/<id>` | GET | **UPDATE** - Estado | Cambia estado completada/pendiente |
| `/eliminar/<id>` | GET | **DELETE** - Eliminar | Elimina la tarea permanentemente |

## 🧪 Datos de Ejemplo

La aplicación incluye 2 tareas de ejemplo:
1. **"Aprender Flask"** - Pendiente
2. **"Hacer la compra"** - Completada

## 💾 Almacenamiento de Datos

```python
# Lista global que simula una base de datos
todos = [
    {
        'id': 1,
        'titulo': 'Aprender Flask',
        'descripcion': 'Completar el tutorial de Flask con templates',
        'completada': False,
        'fecha_creacion': '2024-10-16 10:00:00'
    }
]
```

### 📋 Estructura de cada Tarea
- **`id`**: Número único identificador
- **`titulo`**: Texto principal de la tarea (obligatorio)
- **`descripcion`**: Detalles adicionales (opcional)
- **`completada`**: Estado booleano (True/False)
- **`fecha_creacion`**: Timestamp de cuando se creó

## 🎨 Interfaz de Usuario

- **Bootstrap 5** para diseño responsive
- **Emojis** para mejorar la experiencia visual
- **Colores diferenciados** para estados (verde=completada, amarillo=pendiente)
- **Iconos intuitivos** para acciones (✏️ editar, 🗑️ eliminar, ✅ completar)
- **Mensajes flash** para feedback del usuario

## 🔧 Conceptos Flask Demostrados

### **1. Rutas y Métodos HTTP**
```python
@app.route('/crear', methods=['POST'])
def crear_tarea():
    # Procesa formulario POST
```

### **2. Templates y Herencia**
```html
{% extends "base.html" %}
{% block contenido %}
    <!-- Contenido específico -->
{% endblock %}
```

### **3. Formularios y Validación**
```python
titulo = request.form.get('titulo', '').strip()
if not titulo:
    flash('El título es obligatorio', 'error')
```

### **4. Redirecciones y URL Building**
```python
return redirect(url_for('mostrar_todos'))
```

### **5. Flash Messages**
```python
flash('Tarea creada correctamente', 'success')
```

### **6. Variables de Template**
```python
return render_template('index.html', todos=todos)
```

## 📚 Conceptos Educativos

### **CRUD Operations**
- **C**reate: Añadir nuevas tareas
- **R**ead: Consultar tareas existentes
- **U**pdate: Modificar tareas
- **D**elete: Eliminar tareas

### **HTTP Methods**
- **GET**: Para mostrar páginas y formularios
- **POST**: Para enviar datos de formularios

### **Template Engine (Jinja2)**
- Herencia de templates
- Bloques de contenido
- Variables y filtros
- Estructuras de control (if, for)

### **Web Development Patterns**
- Separación de lógica y presentación
- Formularios HTML
- Validación del lado servidor
- Feedback al usuario
- URLs semánticas

## ⚠️ Limitaciones

1. **Datos en memoria**: Se pierden al reiniciar la aplicación
2. **Sin persistencia**: No hay base de datos real
3. **Sin autenticación**: Todas las tareas son públicas
4. **Sin paginación**: No escalable para muchas tareas
5. **Un solo usuario**: No hay sistema multiusuario

## 🚧 Posibles Mejoras

- Integrar una base de datos (SQLite, PostgreSQL)
- Añadir autenticación de usuarios
- Implementar categorías o etiquetas
- Añadir fechas de vencimiento
- Sistema de prioridades
- Búsqueda y filtros avanzados
- API REST para móviles
- Tests unitarios

## 📝 Notas para Estudiantes

Esta aplicación es perfecta para aprender:
- **Conceptos básicos de Flask**
- **Operaciones CRUD fundamentales**
- **Templates con Jinja2**
- **Formularios HTML**
- **Manejo de estado en aplicaciones web**
- **Estructuras de datos en Python**

---

**¡Ideal para entender los fundamentos del desarrollo web con Flask!** 🎓
