from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Página principal con saludo básico"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', 
                         title='Hello World Flask + Jinja2',
                         current_time=current_time)

@app.route('/about')
def about():
    """Página sobre el proyecto"""
    return render_template('about.html', 
                         title='Acerca de este proyecto')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """Página interactiva con formulario"""
    name = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
    
    return render_template('greet.html', 
                         title='Saludo Personalizado',
                         name=name)

# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
