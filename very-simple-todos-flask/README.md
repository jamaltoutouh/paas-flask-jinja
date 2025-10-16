# Very Simple TODOs Flask - Versión Minimalista

La versión **MÁS SIMPLE POSIBLE** de una aplicación TODOs con Flask. Sin herencia de templates, sin CSS, sin Bootstrap. Solo HTML básico y funcionalidad CRUD esencial.

## 🎯 Características

- ✅ **Crear** tareas nuevas
- 📖 **Ver** lista de todas las tareas  
- ✏️ **Editar** tareas existentes
- 🗑️ **Borrar** tareas
- 🔄 **Marcar** como completada/pendiente

## 📁 Archivos

```
very-simple-todos-flask/
├── app.py                # Aplicación Flask (70 líneas)
└── templates/
    ├── lista.html        # Página principal
    ├── nueva.html        # Crear tarea
    └── editar.html       # Editar tarea
```

## 🚀 Ejecutar

```bash
cd very-simple-todos-flask
python3 app.py
```

Ir a: `http://127.0.0.1:5000/`

## 💾 Datos

```python
# Lista simple en memoria
todos = [
    {'id': 1, 'titulo': 'Aprender Flask', 'completada': False},
    {'id': 2, 'titulo': 'Hacer ejercicio', 'completada': True}
]
```

## 🛠️ Rutas

| URL | Método | Función |
|-----|--------|---------|
| `/` | GET | Ver todas las tareas |
| `/nueva` | GET | Formulario nueva tarea |
| `/crear` | POST | Crear tarea |
| `/editar/<id>` | GET | Formulario editar |
| `/actualizar/<id>` | POST | Actualizar tarea |
| `/completar/<id>` | GET | Cambiar estado |
| `/borrar/<id>` | GET | Eliminar tarea |

## 🎓 Ideal Para Aprender

- Conceptos básicos de Flask
- Rutas y templates simples
- Formularios HTML básicos
- Operaciones CRUD esenciales
- Manejo de listas en Python

## ⚡ Características Simples

- **Sin herencia** de templates
- **Sin CSS** ni estilos
- **Sin JavaScript** complejo
- **Sin base de datos**
- **Sin validaciones** complejas
- **Sin mensajes flash**
- **HTML puro** y básico

## 🔧 Código Minimalista

- Solo **70 líneas** de Python
- Templates de **20-30 líneas** cada uno
- Funciones simples sin decoraciones
- Búsqueda de tareas con bucles básicos
- Formularios HTML estándar

---

**¡La versión más simple para entender Flask desde cero!** 🚀
