#!/bin/bash

# 🚀 Script de comandos útiles para el proyecto Flask + Jinja2

echo "=== 🐍 PROYECTO FLASK + JINJA2 PARA VERCEL ==="
echo ""

# Función para mostrar el menú
show_menu() {
    echo "Selecciona una opción:"
    echo "1. 🏗️  Configurar entorno virtual"
    echo "2. 📦 Instalar dependencias"
    echo "3. 🚀 Ejecutar aplicación localmente"
    echo "4. 🔍 Verificar estructura del proyecto"
    echo "5. 📤 Comandos para subir a GitHub"
    echo "6. 🌐 Información sobre despliegue en Vercel"
    echo "7. 🧪 Ejecutar tests básicos"
    echo "8. 📋 Mostrar URLs importantes"
    echo "9. ❌ Salir"
    echo ""
}

# Función para configurar entorno virtual
setup_venv() {
    echo "🏗️ Configurando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
    echo "Para activarlo ejecuta:"
    echo "  macOS/Linux: source venv/bin/activate"
    echo "  Windows: venv\\Scripts\\activate"
}

# Función para instalar dependencias
install_deps() {
    echo "📦 Instalando dependencias..."
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    pip install -r requirements.txt
    echo "✅ Dependencias instaladas"
}

# Función para ejecutar la aplicación
run_app() {
    echo "🚀 Ejecutando aplicación Flask..."
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    echo "📡 La aplicación estará disponible en: http://localhost:5000"
    echo "🛑 Para detener la aplicación presiona Ctrl+C"
    python app.py
}

# Función para verificar estructura
check_structure() {
    echo "🔍 Verificando estructura del proyecto..."
    echo ""
    echo "📁 Estructura actual:"
    find . -type f -name "*.py" -o -name "*.html" -o -name "*.json" -o -name "*.txt" -o -name "*.md" | head -20
    echo ""
    echo "✅ Archivos críticos:"
    [ -f "app.py" ] && echo "  ✅ app.py" || echo "  ❌ app.py (falta)"
    [ -f "requirements.txt" ] && echo "  ✅ requirements.txt" || echo "  ❌ requirements.txt (falta)"
    [ -f "vercel.json" ] && echo "  ✅ vercel.json" || echo "  ❌ vercel.json (falta)"
    [ -d "templates" ] && echo "  ✅ templates/" || echo "  ❌ templates/ (falta)"
}

# Función para comandos de GitHub
github_commands() {
    echo "📤 Comandos para subir a GitHub:"
    echo ""
    echo "1. Inicializar repositorio:"
    echo "   git init"
    echo ""
    echo "2. Añadir archivos:"
    echo "   git add ."
    echo ""
    echo "3. Primer commit:"
    echo "   git commit -m \"Initial commit: Flask + Jinja2 project\""
    echo ""
    echo "4. Configurar rama principal:"
    echo "   git branch -M main"
    echo ""
    echo "5. Añadir origen remoto (reemplaza <tu-repo>):"
    echo "   git remote add origin https://github.com/<usuario>/<tu-repo>.git"
    echo ""
    echo "6. Subir a GitHub:"
    echo "   git push -u origin main"
}

# Función para información de Vercel
vercel_info() {
    echo "🌐 Información sobre despliegue en Vercel:"
    echo ""
    echo "📋 Pasos para desplegar:"
    echo "1. Sube tu código a GitHub"
    echo "2. Ve a https://vercel.com"
    echo "3. Inicia sesión con GitHub"
    echo "4. Importa tu repositorio"
    echo "5. ¡Vercel detectará automáticamente la configuración!"
    echo ""
    echo "🔧 Archivos importantes para Vercel:"
    echo "  📄 vercel.json - Configuración de despliegue"
    echo "  📄 requirements.txt - Dependencias de Python"
    echo "  📄 app.py - Aplicación principal"
    echo ""
    echo "🔗 Enlaces útiles:"
    echo "  📚 Docs: https://vercel.com/docs"
    echo "  🐍 Python en Vercel: https://vercel.com/docs/functions/serverless-functions/runtimes/python"
}

# Función para tests básicos
run_tests() {
    echo "🧪 Ejecutando tests básicos..."
    echo ""
    
    # Verificar sintaxis de Python
    echo "🔍 Verificando sintaxis de Python..."
    python -m py_compile app.py && echo "  ✅ app.py - Sintaxis OK" || echo "  ❌ app.py - Error de sintaxis"
    
    # Verificar imports
    echo "🔍 Verificando imports..."
    python -c "import flask; print('  ✅ Flask importado correctamente')" 2>/dev/null || echo "  ❌ Error al importar Flask"
    
    # Verificar plantillas
    echo "🔍 Verificando plantillas..."
    [ -f "templates/base.html" ] && echo "  ✅ base.html encontrado" || echo "  ❌ base.html no encontrado"
    [ -f "templates/index.html" ] && echo "  ✅ index.html encontrado" || echo "  ❌ index.html no encontrado"
    [ -f "templates/about.html" ] && echo "  ✅ about.html encontrado" || echo "  ❌ about.html no encontrado"
    [ -f "templates/greet.html" ] && echo "  ✅ greet.html encontrado" || echo "  ❌ greet.html no encontrado"
    
    echo "✅ Tests básicos completados"
}

# Función para mostrar URLs
show_urls() {
    echo "📋 URLs importantes del proyecto:"
    echo ""
    echo "🏠 Desarrollo local:"
    echo "  http://localhost:5000          - Página principal"
    echo "  http://localhost:5000/about    - Información del proyecto"
    echo "  http://localhost:5000/greet    - Formulario de saludo"
    echo ""
    echo "🌐 Recursos útiles:"
    echo "  https://flask.palletsprojects.com/    - Documentación Flask"
    echo "  https://jinja.palletsprojects.com/    - Documentación Jinja2"
    echo "  https://vercel.com/docs               - Documentación Vercel"
    echo "  https://github.com                    - GitHub"
}

# Bucle principal del script
while true; do
    show_menu
    read -p "Ingresa tu opción (1-9): " choice
    echo ""
    
    case $choice in
        1)
            setup_venv
            ;;
        2)
            install_deps
            ;;
        3)
            run_app
            ;;
        4)
            check_structure
            ;;
        5)
            github_commands
            ;;
        6)
            vercel_info
            ;;
        7)
            run_tests
            ;;
        8)
            show_urls
            ;;
        9)
            echo "👋 ¡Hasta luego! Happy coding! 🚀"
            exit 0
            ;;
        *)
            echo "❌ Opción inválida. Por favor selecciona 1-9."
            ;;
    esac
    
    echo ""
    read -p "Presiona Enter para continuar..."
    echo ""
done
