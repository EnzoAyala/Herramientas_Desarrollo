from flask import Blueprint, jsonify, request
from models import db, Usuario
from security import admin_required

api = Blueprint('api', __name__)

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
