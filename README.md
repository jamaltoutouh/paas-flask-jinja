# PaaS Flask Jinja - Proyectos de Enseñanza

Este repositorio contiene varios proyectos educativos para enseñar **Flask**, **templates con Jinja2**, **operaciones CRUD** y **despliegue en la nube**.

## 📁 Estructura del Repositorio

```
paas-flask-jinja/
├── requirements.txt           # Dependencias de Python para todos los proyectos
├── simple-flask/             # 🟢 Proyecto 1: Flask básico
│   └── app.py                # Aplicación Flask "Hello World"
├── template-css-flask/       # 🟡 Proyecto 2: Flask con templates y CSS
│   ├── app.py                # Aplicación con render_template
│   ├── templates/            # Plantillas HTML con herencia
│   ├── static/css/           # Archivos CSS
│   └── README.md             # Documentación detallada
├── simple-todos-flask/       # 🔴 Proyecto 3: Flask CRUD con TODOs
│   ├── app.py                # Aplicación CRUD completa (sin BD)
│   ├── templates/            # Templates para gestión de tareas
│   ├── static/css/           # Estilos con Bootstrap
│   └── README.md             # Documentación del CRUD
└── hello-fly/                # 🔵 Proyecto 4: Node.js para despliegue
    ├── app.js                # Aplicación Express.js
    ├── Dockerfile            # Para contenedorización
    └── fly.toml              # Configuración de Fly.io
```

## 🎯 Objetivos de Aprendizaje

### 📚 **Proyecto 1: simple-flask**
- Conceptos básicos de Flask
- Rutas y funciones de vista
- Variables dinámicas en URLs
- Modo debug

### 📚 **Proyecto 2: template-css-flask**
- Sistema de templates con Jinja2
- Herencia de plantillas (`{% extends %}`)
- Bloques de contenido (`{% block %}`)
- Archivos estáticos (CSS)
- Variables en templates

### 📚 **Proyecto 3: simple-todos-flask** ⭐ **NUEVO**
- **Operaciones CRUD completas** (Create, Read, Update, Delete)
- Formularios HTML con validación
- Gestión de estado sin base de datos
- Flash messages para feedback del usuario
- Bootstrap para UI profesional
- Manejo de listas en Python como almacenamiento

### 📚 **Proyecto 4: hello-fly**
- Aplicación Node.js con Express
- Contenedorización con Docker
- Despliegue en Fly.io
- Configuración de PaaS

## 🚀 Cómo Usar Este Repositorio

### 1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/paas-flask-jinja.git
cd paas-flask-jinja
```

### 2. **Instalar dependencias de Python**
```bash
pip3 install -r requirements.txt
```

### 3. **Ejecutar proyectos individualmente**

#### Simple Flask:
```bash
cd simple-flask
python3 app.py
# Visitar: http://127.0.0.1:5000/
```

#### Flask con Templates:
```bash
cd template-css-flask
python3 app.py
# Visitar: http://127.0.0.1:5000/
```

#### Flask TODOs CRUD:
```bash
cd simple-todos-flask
python3 app.py
# Visitar: http://127.0.0.1:5000/
# ✅ Crear, consultar, actualizar y eliminar tareas
```

#### Node.js Express:
```bash
cd hello-fly
npm install
npm start
# Visitar: http://localhost:3000/
```

## 📋 Requisitos del Sistema

- **Python 3.7+** (para proyectos Flask)
- **Node.js 16+** (para proyecto Express)
- **Git** (para control de versiones)
- **Docker** (opcional, para contenedorización)

## 🛠️ Tecnologías Utilizadas

| Proyecto | Tecnologías | Concepto Principal |
|----------|-------------|-------------------|
| **simple-flask** | Python, Flask | Fundamentos básicos |
| **template-css-flask** | Python, Flask, Jinja2, HTML, CSS | Templates y herencia |
| **simple-todos-flask** | Python, Flask, Bootstrap, Jinja2 | **Operaciones CRUD** |
| **hello-fly** | Node.js, Express.js, Docker, Fly.io | Despliegue en nube |

## 🔥 **Destacado: Aplicación TODOs CRUD**

La nueva aplicación `simple-todos-flask` es perfecta para aprender:

### ✅ **Funcionalidades CRUD Implementadas:**
- **CREATE**: Crear nuevas tareas con formularios
- **READ**: Listar todas las tareas + vista individual detallada
- **UPDATE**: Editar tareas + cambiar estado (completada/pendiente)
- **DELETE**: Eliminar tareas con confirmación

### 🎨 **Características de la UI:**
- Diseño moderno con **Bootstrap 5**
- **Tarjetas interactivas** para cada tarea
- **Iconos intuitivos** para acciones
- **Colores diferenciados** por estado
- **Estadísticas en tiempo real**
- **Mensajes flash** para feedback

### 🔧 **Conceptos Flask Avanzados:**
- Múltiples rutas con diferentes métodos HTTP
- Formularios POST con validación
- Redirecciones y `url_for()`
- Flash messages con categorías
- Variables globales para almacenamiento
- Manejo de errores 404

## 📖 Progresión de Aprendizaje Recomendada

1. **🟢 simple-flask** → Conceptos básicos de Flask
2. **🟡 template-css-flask** → Templates y presentación
3. **🔴 simple-todos-flask** → CRUD y lógica de negocio
4. **🔵 hello-fly** → Despliegue y producción

## 📚 Recursos Adicionales

- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- [Guía de Jinja2](https://jinja.palletsprojects.com/)
- [Tutorial de Bootstrap](https://getbootstrap.com/docs/)
- [Documentación de Fly.io](https://fly.io/docs/)

## 👨‍🏫 Uso Educativo

Este repositorio está diseñado para cursos de:
- **Desarrollo Web con Python**
- **Frameworks web modernos**
- **Operaciones CRUD en aplicaciones web**
- **Templates y diseño frontend**
- **Despliegue en la nube (PaaS)**
- **DevOps básico**

## 🎓 Para Estudiantes

### **Orden de Estudio Sugerido:**
1. Ejecuta `simple-flask` para entender las bases
2. Explora `template-css-flask` para aprender templates
3. **Estudia a fondo `simple-todos-flask`** para dominar CRUD
4. Finalmente `hello-fly` para aprender despliegue

### **Actividades Propuestas:**
- Modifica las aplicaciones existentes
- Añade nuevas funcionalidades a la app TODOs
- Crea tus propias rutas y templates
- Practica el despliegue con diferentes servicios

## 📝 Licencia

Este proyecto es de uso educativo. Siéntete libre de usar, modificar y distribuir para fines de aprendizaje.

---

**¡Perfecto para aprender desarrollo web desde lo básico hasta el despliegue, incluyendo operaciones CRUD completas!** 🎓
