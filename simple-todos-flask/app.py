# app.py - Aplicación Flask simple para gestionar TODOs sin base de datos

# Importar Flask y funciones necesarias
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Clave secreta para usar flash messages (mensajes temporales)
app.secret_key = 'mi_clave_secreta_para_todos'

# Lista global para almacenar las tareas (simula una base de datos)
# Cada tarea es un diccionario con: id, titulo, descripcion, completada, fecha_creacion
todos = [
    {
        'id': 1,
        'titulo': 'Aprender Flask',
        'descripcion': 'Completar el tutorial de Flask con templates',
        'completada': False,
        'fecha_creacion': '2024-10-16 10:00:00'
    },
    {
        'id': 2,
        'titulo': 'Hacer la compra',
        'descripcion': 'Comprar leche, pan y huevos',
        'completada': True,
        'fecha_creacion': '2024-10-15 15:30:00'
    }
]

# Variable para generar IDs únicos
siguiente_id = 3


# RUTA: Mostrar todas las tareas (READ)
@app.route('/')
def mostrar_todos():
    """
    Página principal que muestra todas las tareas
    
    Returns:
        str: HTML renderizado con la lista de tareas
    """
    return render_template('index.html', 
                         todos=todos,
                         total_tareas=len(todos),
                         tareas_completadas=len([t for t in todos if t['completada']]))


# RUTA: Mostrar formulario para crear nueva tarea
@app.route('/nueva')
def nueva_tarea_form():
    """
    Muestra el formulario para crear una nueva tarea
    
    Returns:
        str: HTML renderizado con el formulario
    """
    return render_template('nueva_tarea.html')


# RUTA: Crear nueva tarea (CREATE)
@app.route('/crear', methods=['POST'])
def crear_tarea():
    """
    Procesa el formulario y crea una nueva tarea
    
    Returns:
        redirect: Redirección a la página principal
    """
    global siguiente_id
    
    # Obtener datos del formulario
    titulo = request.form.get('titulo', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    
    # Validar que el título no esté vacío
    if not titulo:
        flash('El título es obligatorio', 'error')
        return redirect(url_for('nueva_tarea_form'))
    
    # Crear nueva tarea
    nueva_tarea = {
        'id': siguiente_id,
        'titulo': titulo,
        'descripcion': descripcion if descripcion else 'Sin descripción',
        'completada': False,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Añadir la tarea a la lista
    todos.append(nueva_tarea)
    siguiente_id += 1
    
    # Mensaje de confirmación
    flash(f'Tarea "{titulo}" creada correctamente', 'success')
    return redirect(url_for('mostrar_todos'))


# RUTA: Mostrar formulario para editar tarea
@app.route('/editar/<int:tarea_id>')
def editar_tarea_form(tarea_id):
    """
    Muestra el formulario para editar una tarea existente
    
    Args:
        tarea_id (int): ID de la tarea a editar
        
    Returns:
        str: HTML renderizado con el formulario de edición
    """
    # Buscar la tarea por ID
    tarea = next((t for t in todos if t['id'] == tarea_id), None)
    
    if not tarea:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('mostrar_todos'))
    
    return render_template('editar_tarea.html', tarea=tarea)


# RUTA: Actualizar tarea existente (UPDATE)
@app.route('/actualizar/<int:tarea_id>', methods=['POST'])
def actualizar_tarea(tarea_id):
    """
    Procesa el formulario y actualiza una tarea existente
    
    Args:
        tarea_id (int): ID de la tarea a actualizar
        
    Returns:
        redirect: Redirección a la página principal
    """
    # Buscar la tarea por ID
    tarea = next((t for t in todos if t['id'] == tarea_id), None)
    
    if not tarea:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('mostrar_todos'))
    
    # Obtener datos del formulario
    titulo = request.form.get('titulo', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    
    # Validar que el título no esté vacío
    if not titulo:
        flash('El título es obligatorio', 'error')
        return redirect(url_for('editar_tarea_form', tarea_id=tarea_id))
    
    # Actualizar la tarea
    tarea['titulo'] = titulo
    tarea['descripcion'] = descripcion if descripcion else 'Sin descripción'
    
    # Mensaje de confirmación
    flash(f'Tarea "{titulo}" actualizada correctamente', 'success')
    return redirect(url_for('mostrar_todos'))


# RUTA: Marcar tarea como completada/pendiente
@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    """
    Cambia el estado de completado de una tarea
    
    Args:
        tarea_id (int): ID de la tarea a cambiar
        
    Returns:
        redirect: Redirección a la página principal
    """
    # Buscar la tarea por ID
    tarea = next((t for t in todos if t['id'] == tarea_id), None)
    
    if not tarea:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('mostrar_todos'))
    
    # Cambiar el estado
    tarea['completada'] = not tarea['completada']
    estado = 'completada' if tarea['completada'] else 'pendiente'
    
    flash(f'Tarea marcada como {estado}', 'success')
    return redirect(url_for('mostrar_todos'))


# RUTA: Eliminar tarea (DELETE)
@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    """
    Elimina una tarea de la lista
    
    Args:
        tarea_id (int): ID de la tarea a eliminar
        
    Returns:
        redirect: Redirección a la página principal
    """
    global todos
    
    # Buscar la tarea por ID
    tarea = next((t for t in todos if t['id'] == tarea_id), None)
    
    if not tarea:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('mostrar_todos'))
    
    # Eliminar la tarea de la lista
    todos = [t for t in todos if t['id'] != tarea_id]
    
    flash(f'Tarea "{tarea["titulo"]}" eliminada correctamente', 'success')
    return redirect(url_for('mostrar_todos'))


# RUTA: Ver detalles de una tarea específica
@app.route('/tarea/<int:tarea_id>')
def ver_tarea(tarea_id):
    """
    Muestra los detalles completos de una tarea
    
    Args:
        tarea_id (int): ID de la tarea a mostrar
        
    Returns:
        str: HTML renderizado con los detalles de la tarea
    """
    # Buscar la tarea por ID
    tarea = next((t for t in todos if t['id'] == tarea_id), None)
    
    if not tarea:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('mostrar_todos'))
    
    return render_template('detalle_tarea.html', tarea=tarea)


# Punto de entrada principal
if __name__ == '__main__':
    """
    Ejecutar la aplicación en modo debug
    """
    print("🚀 Iniciando aplicación TODOs Flask...")
    print("📝 Funcionalidades disponibles:")
    print("   ✅ Crear tareas")
    print("   📖 Consultar tareas") 
    print("   ✏️  Actualizar tareas")
    print("   🗑️  Borrar tareas")
    print("   🔄 Marcar como completada/pendiente")
    print("\n🌐 Accede a: http://127.0.0.1:5000/")
    
    app.run(debug=True)
