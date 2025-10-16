# app.py - Aplicación Flask simple con templates

# Importar Flask y render_template para usar plantillas HTML
from flask import Flask, render_template

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal - página de inicio
@app.route('/')
def home():
    """
    Página de inicio que usa el template index.html
    
    Returns:
        str: HTML renderizado desde template
    """
    return render_template('index.html', 
                         titulo="Mi App Flask",
                         mensaje="¡Hola, mundo con templates!")

# Punto de entrada principal
if __name__ == '__main__':
    """
    Ejecutar la aplicación en modo debug
    """
    app.run(debug=True)
