# app.py - Aplicación Flask MUY SIMPLE para TODOs sin herencia ni CSS

from flask import Flask, render_template, request, redirect, url_for

# Crear aplicación Flask
app = Flask(__name__)

# Lista simple para guardar tareas en memoria
todos = [
    {'id': 1, 'titulo': 'Aprender Flask', 'completada': False},
    {'id': 2, 'titulo': 'Hacer ejercicio', 'completada': True}
]

# Variable para IDs únicos
siguiente_id = 3


# PÁGINA PRINCIPAL: Ver todas las tareas
@app.route('/')
def lista():
    """Mostrar todas las tareas"""
    return render_template('lista.html', todos=todos)


# PÁGINA: Formulario para nueva tarea
@app.route('/nueva')
def nueva():
    """Mostrar formulario para crear tarea"""
    return render_template('nueva.html')


# ACCIÓN: Crear nueva tarea
@app.route('/crear', methods=['POST'])
def crear():
    """Crear nueva tarea"""
    global siguiente_id
    
    titulo = request.form['titulo']
    if titulo:  # Solo si tiene título
        nueva_tarea = {
            'id': siguiente_id,
            'titulo': titulo,
            'completada': False
        }
        todos.append(nueva_tarea)
        siguiente_id += 1
    
    return redirect(url_for('lista'))


# PÁGINA: Formulario para editar tarea
@app.route('/editar/<int:tarea_id>')
def editar(tarea_id):
    """Mostrar formulario para editar tarea"""
    # Buscar la tarea por ID
    tarea = None
    for t in todos:
        if t['id'] == tarea_id:
            tarea = t
            break
    
    if tarea:
        return render_template('editar.html', tarea=tarea)
    else:
        return redirect(url_for('lista'))


# ACCIÓN: Actualizar tarea
@app.route('/actualizar/<int:tarea_id>', methods=['POST'])
def actualizar(tarea_id):
    """Actualizar tarea existente"""
    titulo = request.form['titulo']
    
    # Buscar y actualizar la tarea
    for tarea in todos:
        if tarea['id'] == tarea_id:
            if titulo:  # Solo si tiene título
                tarea['titulo'] = titulo
            break
    
    return redirect(url_for('lista'))


# ACCIÓN: Cambiar estado de completada
@app.route('/completar/<int:tarea_id>')
def completar(tarea_id):
    """Marcar tarea como completada o pendiente"""
    # Buscar y cambiar estado
    for tarea in todos:
        if tarea['id'] == tarea_id:
            tarea['completada'] = not tarea['completada']
            break
    
    return redirect(url_for('lista'))


# ACCIÓN: Eliminar tarea
@app.route('/borrar/<int:tarea_id>')
def borrar(tarea_id):
    """Eliminar tarea"""
    global todos
    
    # Filtrar la lista para quitar la tarea
    todos = [t for t in todos if t['id'] != tarea_id]
    
    return redirect(url_for('lista'))


# Ejecutar aplicación
if __name__ == '__main__':
    print("🚀 TODOs Flask Súper Simple")
    print("📝 Accede a: http://127.0.0.1:5000/")
    app.run(debug=True)
