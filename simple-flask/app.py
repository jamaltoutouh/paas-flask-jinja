# app.py - Una aplicación Flask simple de "Hello World"

# Importar la clase Flask desde el paquete flask
# Flask es el framework web que usaremos para crear nuestra aplicación
from flask import Flask

# Crear una instancia de la aplicación Flask
# Flask usa esto para determinar la ubicación de la aplicación y encontrar recursos como templates y archivos estáticos
app = Flask(__name__)

# Definir una ruta usando el decorador @app.route()
# El decorador asocia la función con una URL específica
# En este caso, '/' representa la página principal (home) del sitio web
@app.route('/')
def hello_world():
    """
    Función de vista que maneja las peticiones GET a la URL raíz ('/')
    
    Returns:
        str: Una cadena de texto HTML que se enviará al navegador del usuario
    """
    # Esta función se ejecutará cuando alguien visite la página principal
    # Retorna una cadena de texto que será mostrada en el navegador
    return '<h1>¡Hola, Mundo!</h1><p>Esta es mi primera aplicación Flask.</p>'

# Ruta adicional para demostrar múltiples endpoints
@app.route('/saludo')
def saludo():
    """
    Función de vista para una segunda ruta
    
    Returns:
        str: Un mensaje de saludo personalizado
    """
    return '<h2>¡Saludos desde Flask!</h2><p>Esta es otra ruta en nuestra aplicación.</p>'

# Ruta con parámetro dinámico
@app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    """
    Función de vista que acepta un parámetro dinámico en la URL
    
    Args:
        nombre (str): El nombre del usuario capturado de la URL
        
    Returns:
        str: Un mensaje personalizado con el nombre del usuario
    """
    # El parámetro <nombre> en la ruta se pasa como argumento a la función
    return f'<h2>¡Hola, {nombre}!</h2><p>Bienvenido a nuestra aplicación Flask.</p>'

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    """
    Este bloque se ejecuta solo si el archivo se ejecuta directamente
    (no cuando se importa como módulo en otro archivo)
    """
    # Ejecutar la aplicación Flask en modo debug
    # debug=True permite:
    # - Recarga automática cuando se cambia el código
    # - Mensajes de error detallados en el navegador
    # - No usar debug=True en producción por seguridad
    app.run(debug=True)
    
    # Por defecto, Flask ejecuta en:
    # - Host: 127.0.0.1 (localhost)
    # - Puerto: 5000
    # - URL completa: http://127.0.0.1:5000/
    # -- Puedes probar con http://127.0.0.1:5000/saludo y http://127.0.0.1:5000/usuario/<nombre>
