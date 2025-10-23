# 🚀 Flask + Jinja2 - Proyecto para Vercel

Un proyecto educativo simple que demuestra cómo crear y desplegar una aplicación web usando Flask, Jinja2 y Vercel.

## 📋 Descripción

Este proyecto es ideal para aprender:
- Desarrollo web con Python y Flask
- Plantillas dinámicas con Jinja2
- Despliegue gratuito en Vercel
- Integración con GitHub para CI/CD

## 🛠️ Tecnologías

- **Python 3.x** - Lenguaje de programación
- **Flask 2.3.3** - Framework web minimalista
- **Jinja2 3.1.2** - Motor de plantillas
- **Vercel** - Plataforma de despliegue
- **GitHub** - Control de versiones

## 📁 Estructura del Proyecto

```
vercel-deployment/
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias de Python
├── vercel.json        # Configuración de Vercel
├── templates/         # Plantillas Jinja2
│   ├── base.html      # Plantilla base
│   ├── index.html     # Página principal
│   ├── about.html     # Página de información
│   └── greet.html     # Página de saludo interactiva
└── README.md          # Este archivo
```

## 🚀 Cómo ejecutar localmente

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd vercel-deployment
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 🌐 Desplegar en Vercel

### Método 1: Desde GitHub (Recomendado)

1. **Subir código a GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <tu-repositorio-github>
   git push -u origin main
   ```

2. **Conectar con Vercel**
   - Ve a [vercel.com](https://vercel.com)
   - Inicia sesión con GitHub
   - Importa tu repositorio
   - ¡Vercel detectará automáticamente la configuración!

### Método 2: Vercel CLI

1. **Instalar Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Desplegar**
   ```bash
   vercel
   ```

## 📚 Conceptos que aprenderás

### Flask
- Rutas y vistas
- Manejo de formularios
- Métodos HTTP (GET, POST)
- Renderizado de plantillas

### Jinja2
- Herencia de plantillas (`{% extends %}`)
- Bloques de contenido (`{% block %}`)
- Variables (`{{ variable }}`)
- Estructuras de control (`{% if %}`, `{% for %}`)
- Filtros y funciones

### Vercel
- Configuración con `vercel.json`
- Despliegue automático desde GitHub
- Variables de entorno
- Dominios personalizados

## 🎯 Características del proyecto

✅ **Página principal** - Introducción al proyecto  
✅ **Página de información** - Documentación técnica  
✅ **Formulario interactivo** - Demostración de Jinja2  
✅ **Diseño responsivo** - Compatible con móviles  
✅ **Navegación fluida** - Enlaces entre páginas  
✅ **Código comentado** - Fácil de entender  

## 🔧 Archivos importantes

### `app.py`
Contiene la lógica principal de Flask con tres rutas:
- `/` - Página principal
- `/about` - Información del proyecto  
- `/greet` - Formulario interactivo

### `vercel.json`
Configuración para el despliegue en Vercel:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### `requirements.txt`
Lista las dependencias de Python necesarias para el proyecto.

## 🐛 Solución de problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "Port already in use"
```bash
# Cambiar el puerto en app.py o terminar el proceso
lsof -ti:5000 | xargs kill
```

### Error en Vercel: "Build failed"
- Verificar que `vercel.json` esté en la raíz
- Comprobar que `requirements.txt` contenga todas las dependencias
- Revisar los logs de Vercel para detalles específicos

## 📖 Recursos adicionales

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de Jinja2](https://jinja.palletsprojects.com/)
- [Guía de Vercel para Python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Tutorial de Git y GitHub](https://docs.github.com/es/get-started)

## 👨‍💻 Ejercicios propuestos

1. **Añadir una nueva página** con su propia ruta y plantilla
2. **Implementar un contador de visitas** usando variables de sesión
3. **Crear un formulario de contacto** con validación
4. **Añadir estilos CSS personalizados** en un archivo separado
5. **Implementar una API REST** simple con Flask

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

🎓 **Proyecto educativo creado para enseñar desarrollo web con Python**
