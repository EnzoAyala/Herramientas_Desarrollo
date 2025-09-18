from flask import Blueprint, jsonify, request
from models import db, Usuario, Categoria
from security import admin_required
from werkzeug.exceptions import BadRequest

api = Blueprint('api', __name__)

# METODOS DE USUARIO ---------------------------------------------------------------------------------
@api.route('/users', methods=['GET'])
@admin_required
def get_users():
    users = Usuario.query.all()
    users_data = [{
        'id': user.id,
        'nombre': user.nombre,
        'apellido': user.apellido,
        'correo': user.correo,
        'rol_id': user.rol_id
    } for user in users]
    return jsonify(users_data)

@api.route('/users/<int:user_id>/role', methods=['PUT'])
@admin_required
def update_user_role(user_id):
    user = Usuario.query.get_or_404(user_id)
    data = request.get_json()
    
    try:
        new_rol_id = int(data.get('rol_id'))
    except (ValueError, TypeError):
        return jsonify({'error': 'El ID de rol debe ser un número'}), 400

    if new_rol_id not in [1, 2]: # Asumiendo que 1 es usuario y 2 es admin
        return jsonify({'error': 'ID de rol inválido'}), 400

    user.rol_id = new_rol_id
    db.session.commit()
    return jsonify({'message': 'Rol de usuario actualizado correctamente'})

@api.route('/users/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(user_id):
    user = Usuario.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado correctamente'})
# ---------------------------------------------------------------------------------------------------------

# METODOS DE CATEGORIA ---------------------------------------------------------------------------------
@api.route('/categoria/get', methods=['GET'])
def get_categoria():
    categorias = Categoria.query.all()
    categoria_data = [{
        'id': categoria.id,
        'nombre': categoria.nombre,
        'imagen': categoria.imagen
    } for categoria in categorias]
    return jsonify(categoria_data), 200

@api.route('/categoria/add', methods=['POST'])
@admin_required
def add_categoria():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        imagen = data.get('imagen')

        if not nombre or not imagen:
            raise BadRequest('Los campos nombre y imagen son obligatorios')
        
        nueva_categoria = Categoria(nombre=nombre, imagen=imagen)
        db.session.add(nueva_categoria)
        db.session.commit()
        return jsonify({'message': 'Categoria agregada correctamente'}), 201
    
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error al agregar la categoria'}), 500

@api.route('/categoria/modify/<int:categoria_id>', methods=['PUT'])
@admin_required
def modify_categoria(categoria_id):
    try: 
        categoria = Categoria.query.get_or_404(categoria_id)
        data = request.get_json()

        nombre = data.get('nombre')
        imagen = data.get('imagen')

        if not nombre or not imagen:
            raise BadRequest('Los campos nombre y imagen son obligatorios')
        
        categoria.nombre = nombre
        categoria.imagen = imagen
        db.session.commit()
        return jsonify({'message': 'Categoria modificada correctamente'}), 200
    
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error al modificar la categoria'}), 500
        

@api.route('/categoria/remove/<int:categoria_id>', methods=['DELETE'])
@admin_required
def remove_categoria(categoria_id):
    try:
        categoria = Categoria.query.get_or_404(categoria_id)
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({'message': 'Categoria eliminada correctamente'}), 200
    
    except Exception as e:
        return jsonify({'error': 'Error al eliminar la categoria'}), 500
# ---------------------------------------------------------------------------------------------------------