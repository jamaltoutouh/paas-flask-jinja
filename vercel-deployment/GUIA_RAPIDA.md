# 🎯 GUÍA RÁPIDA PARA ESTUDIANTES

## 🚀 Inicio Rápido (5 minutos)

### 1. Preparar el entorno
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar localmente
```bash
python app.py
```
Abre: http://localhost:5001

### 3. Subir a GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

### 4. Desplegar en Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Conecta tu cuenta de GitHub
3. Importa tu repositorio
4. ¡Listo! Tu app estará online

---

## 📚 Conceptos Clave

### Flask Routes
```python
@app.route('/')           # GET por defecto
@app.route('/form', methods=['GET', 'POST'])  # GET y POST
```

### Jinja2 Templates
```html
{{ variable }}                    <!-- Mostrar variable -->
{% if condition %}...{% endif %}  <!-- Condicional -->
{% for item in items %}...{% endfor %}  <!-- Bucle -->
{% extends "base.html" %}         <!-- Herencia -->
{% block content %}...{% endblock %}  <!-- Bloque -->
```

### Estructura de Archivos
```
proyecto/
├── app.py              # Lógica principal
├── requirements.txt    # Dependencias
├── vercel.json        # Config Vercel
└── templates/         # HTML templates
    ├── base.html      # Template base
    └── index.html     # Página específica
```

---

## 🛠️ Comandos Útiles

### Desarrollo Local
```bash
# Instalar nueva dependencia
pip install <paquete>
pip freeze > requirements.txt

# Verificar sintaxis
python -m py_compile app.py

# Debugging
export FLASK_DEBUG=1  # o set FLASK_DEBUG=1 en Windows
python app.py
```

### Git & GitHub
```bash
# Ver estado
git status

# Añadir cambios
git add .
git commit -m "Descripción del cambio"
git push

# Ver historial
git log --oneline
```

### Vercel
```bash
# Instalar CLI (opcional)
npm i -g vercel

# Desplegar directamente
vercel

# Ver logs
vercel logs
```

---

## 🐛 Solución de Problemas

### ❌ "Module not found"
```bash
pip install -r requirements.txt
```

### ❌ "Port 5001 in use"
```bash
# Cambiar puerto en app.py:
app.run(port=5002)

# O terminar proceso:
lsof -ti:5001 | xargs kill
```

### ❌ "Template not found"
- Verificar que el archivo esté en `templates/`
- Verificar el nombre exacto del archivo
- Verificar que no haya errores de sintaxis en el template

### ❌ Vercel build fails
- Verificar `vercel.json` en la raíz
- Verificar `requirements.txt` completo
- Revisar logs en el dashboard de Vercel

---

## 🎯 Ejercicios Sugeridos

### Nivel 1: Básico
1. Cambiar el título de la página principal
2. Añadir tu nombre en el footer
3. Cambiar los colores del CSS

### Nivel 2: Intermedio
1. Crear una nueva página `/contact`
2. Añadir un formulario de contacto
3. Mostrar la fecha actual en formato español

### Nivel 3: Avanzado
1. Implementar un contador de visitas
2. Añadir validación de formularios
3. Crear una pequeña API REST
4. Añadir una base de datos SQLite

---

## 📖 Referencias Rápidas

### Flask
- [Documentación oficial](https://flask.palletsprojects.com/)
- [Guía de inicio rápido](https://flask.palletsprojects.com/quickstart/)

### Jinja2
- [Documentación](https://jinja.palletsprojects.com/)
- [Template Designer](https://jinja.palletsprojects.com/templates/)

### Vercel
- [Documentación](https://vercel.com/docs)
- [Python en Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

### Git/GitHub
- [Guía de Git](https://git-scm.com/docs)
- [GitHub Docs](https://docs.github.com/)

---

🎓 **¡Happy Coding!** 🚀
























































































































































































🎓 **¡Happy Coding!** 🚀---- [GitHub Docs](https://docs.github.com/)- [Guía de Git](https://git-scm.com/docs)### Git/GitHub- [Python en Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)- [Documentación](https://vercel.com/docs)### Vercel- [Template Designer](https://jinja.palletsprojects.com/templates/)- [Documentación](https://jinja.palletsprojects.com/)### Jinja2- [Guía de inicio rápido](https://flask.palletsprojects.com/quickstart/)- [Documentación oficial](https://flask.palletsprojects.com/)### Flask## 📖 Referencias Rápidas---4. Añadir una base de datos SQLite3. Crear una pequeña API REST2. Añadir validación de formularios1. Implementar un contador de visitas### Nivel 3: Avanzado3. Mostrar la fecha actual en formato español2. Añadir un formulario de contacto1. Crear una nueva página `/contact`### Nivel 2: Intermedio3. Cambiar los colores del CSS2. Añadir tu nombre en el footer1. Cambiar el título de la página principal### Nivel 1: Básico## 🎯 Ejercicios Sugeridos---- Revisar logs en el dashboard de Vercel- Verificar `requirements.txt` completo- Verificar `vercel.json` en la raíz### ❌ Vercel build fails- Verificar que no haya errores de sintaxis en el template- Verificar el nombre exacto del archivo- Verificar que el archivo esté en `templates/`### ❌ "Template not found"```lsof -ti:5000 | xargs kill# O terminar proceso:app.run(port=5001)# Cambiar puerto en app.py:```bash### ❌ "Port 5000 in use"```pip install -r requirements.txt```bash### ❌ "Module not found"## 🐛 Solución de Problemas---```vercel logs# Ver logsvercel# Desplegar directamentenpm i -g vercel# Instalar CLI (opcional)```bash### Vercel```git log --oneline# Ver historialgit pushgit commit -m "Descripción del cambio"git add .# Añadir cambiosgit status# Ver estado```bash### Git & GitHub```python app.pyexport FLASK_DEBUG=1  # o set FLASK_DEBUG=1 en Windows# Debuggingpython -m py_compile app.py# Verificar sintaxispip freeze > requirements.txtpip install <paquete># Instalar nueva dependencia```bash### Desarrollo Local## 🛠️ Comandos Útiles---```    └── index.html     # Página específica    ├── base.html      # Template base└── templates/         # HTML templates├── vercel.json        # Config Vercel├── requirements.txt    # Dependencias├── app.py              # Lógica principalproyecto/```### Estructura de Archivos```{% block content %}...{% endblock %}  <!-- Bloque -->{% extends "base.html" %}         <!-- Herencia -->{% for item in items %}...{% endfor %}  <!-- Bucle -->{% if condition %}...{% endif %}  <!-- Condicional -->{{ variable }}                    <!-- Mostrar variable -->```html### Jinja2 Templates```@app.route('/form', methods=['GET', 'POST'])  # GET y POST@app.route('/')           # GET por defecto```python### Flask Routes## 📚 Conceptos Clave---4. ¡Listo! Tu app estará online3. Importa tu repositorio2. Conecta tu cuenta de GitHub1. Ve a [vercel.com](https://vercel.com)### 4. Desplegar en Vercel```git push -u origin maingit remote add origin https://github.com/tu-usuario/tu-repo.gitgit branch -M maingit commit -m "Initial commit"git add .git init```bash### 3. Subir a GitHubAbre: http://localhost:5000```python app.py```bash### 2. Ejecutar localmente```pip install -r requirements.txt# Instalar dependencias# venv\Scripts\activate   # Windowssource venv/bin/activate  # macOS/Linux# Activar entorno virtualpython3 -m venv venv# Crear entorno virtual```bash### 1. Preparar el entorno## 🚀 Inicio Rápido (5 minutos)noteId: "da4354f0afe611f09beed12b5ee6c17e"
tags: []

---

