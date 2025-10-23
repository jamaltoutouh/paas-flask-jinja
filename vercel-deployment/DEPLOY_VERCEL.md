# 🚀 Guía de Despliegue en Vercel

Esta guía te ayudará a desplegar tu aplicación Flask + Jinja2 en Vercel de forma gratuita.

## 📋 Prerrequisitos

- ✅ Código del proyecto completo
- ✅ Cuenta de GitHub
- ✅ Cuenta de Vercel (gratis)

## 🛠️ Archivos necesarios para Vercel

### 1. `vercel.json` - Configuración principal
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

### 2. `requirements.txt` - Dependencias de Python
```
Flask==2.3.3
Jinja2==3.1.2
```

### 3. `runtime.txt` - Versión de Python (opcional)
```
python-3.9
```

## 🚀 Proceso de Despliegue

### Método 1: Desde GitHub (Recomendado)

#### Paso 1: Subir código a GitHub
```bash
# Inicializar repositorio
git init

# Añadir archivos
git add .

# Primer commit
git commit -m "Initial commit: Flask + Jinja2 for Vercel"

# Configurar rama principal
git branch -M main

# Añadir repositorio remoto (reemplaza con tu repo)
git remote add origin https://github.com/tu-usuario/tu-repositorio.git

# Subir código
git push -u origin main
```

#### Paso 2: Conectar con Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Haz clic en "Sign up" o "Login"
3. Selecciona "Continue with GitHub"
4. Autoriza a Vercel para acceder a tus repositorios
5. En el dashboard, haz clic en "New Project"
6. Busca y selecciona tu repositorio
7. Haz clic en "Import"

#### Paso 3: Configuración automática
- Vercel detectará automáticamente que es un proyecto Python
- No necesitas cambiar nada en la configuración
- Haz clic en "Deploy"

#### Paso 4: ¡Listo!
- Vercel construirá y desplegará tu aplicación
- Te dará una URL como: `https://tu-proyecto.vercel.app`
- Cada push a GitHub actualizará automáticamente la aplicación

### Método 2: Vercel CLI

#### Instalar Vercel CLI
```bash
npm install -g vercel
```

#### Desplegar
```bash
# En el directorio del proyecto
vercel

# Seguir las instrucciones en pantalla
# Primera vez: configurar proyecto
# Siguientes veces: despliegue automático
```

## 🔧 Configuraciones avanzadas

### Variables de entorno
Si necesitas variables de entorno:

1. En el dashboard de Vercel, ve a tu proyecto
2. Settings > Environment Variables
3. Añade tus variables:
   - `FLASK_ENV=production`
   - `SECRET_KEY=tu-clave-secreta`

### Dominios personalizados
1. Settings > Domains
2. Añadir tu dominio personalizado
3. Configurar DNS según las instrucciones

### Logs y monitoreo
- Functions > View Function Logs
- Analytics para ver estadísticas de uso
- Speed Insights para rendimiento

## 🐛 Solución de problemas comunes

### Error: "Build failed"
**Posibles causas:**
- `vercel.json` no está en la raíz del proyecto
- `requirements.txt` falta dependencias
- Errores de sintaxis en Python

**Solución:**
```bash
# Verificar estructura
ls -la

# Verificar sintaxis
python -m py_compile app.py

# Verificar dependencias
pip install -r requirements.txt
```

### Error: "Module not found"
**Causa:** Falta una dependencia en `requirements.txt`

**Solución:**
```bash
# Actualizar requirements.txt
pip freeze > requirements.txt

# Commit y push
git add requirements.txt
git commit -m "Update requirements.txt"
git push
```

### Error: "Function timeout"
**Causa:** Función tarda más de 10 segundos (límite gratuito)

**Solución:**
- Optimizar código
- Usar caché
- Considerar plan de pago para más tiempo

### Error: "404 Not Found"
**Causa:** Rutas mal configuradas

**Solución:**
Verificar `vercel.json`:
```json
{
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

## 📊 Límites del plan gratuito

- ✅ 100GB de ancho de banda por mes
- ✅ 1000 invocaciones de función por mes
- ✅ 10 segundos de timeout por función
- ✅ 512MB de memoria por función
- ✅ Dominios personalizados
- ✅ SSL automático
- ✅ CDN global

## 🚀 Optimizaciones para producción

### 1. Manejo de errores
```python
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
```

### 2. Configuración de producción
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

app.config.from_object(Config)
```

### 3. Compresión y caché
```python
from flask import Flask
from datetime import timedelta

app = Flask(__name__)

# Cache headers para archivos estáticos
@app.after_request
def after_request(response):
    if request.endpoint == 'static':
        response.cache_control.max_age = 86400  # 1 día
    return response
```

## 📚 Recursos adicionales

- [Documentación oficial de Vercel](https://vercel.com/docs)
- [Python en Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Ejemplos de proyectos](https://github.com/vercel/examples/tree/main/python)
- [Comunidad de Vercel](https://vercel.com/community)

## 🎯 Checklist pre-despliegue

- [ ] `app.py` funciona localmente
- [ ] `requirements.txt` actualizado
- [ ] `vercel.json` configurado
- [ ] Templates en directorio `templates/`
- [ ] `.gitignore` configurado
- [ ] Código subido a GitHub
- [ ] Sin errores de sintaxis
- [ ] Rutas probadas localmente

---

¡Feliz despliegue! 🎉
