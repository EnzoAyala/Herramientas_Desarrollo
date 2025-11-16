from flask import Blueprint, jsonify, request
from models import db, Usuario, Categoria, Producto
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

# METODOS DE PRODUCTO ---------------------------------------------------------------------------------
@api.route('/producto/get', methods=['GET'])
def get_productos():
    productos = Producto.query.all()

    if not productos:
        return jsonify({'mensaje': 'No hay productos disponibles'}), 200

    producto_data = [{
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        'imagen': producto.imagen,
        'categoria_id': producto.categoria_id,
        'modelo_id': producto.modelo_id,
        'almacenamiento_id': producto.almacenamiento_id,
        'color_id': producto.color_id,
        'stock': producto.stock,
        'procesador': producto.procesador,
        'camara': producto.camara,
        'bateria': producto.bateria,
        'pantalla': producto.pantalla,
        'memoria': producto.memoria
    } for producto in productos]

    return jsonify(producto_data), 200

@api.route('/producto/add', methods=['POST'])
@admin_required
def add_producto():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        imagen = data.get('imagen')
        categoria_id = data.get('categoria_id')
        modelo_id = data.get('modelo_id')
        almacenamiento_id = data.get('almacenamiento_id')
        color_id = data.get('color_id')
        stock = data.get('stock')
        procesador = data.get('procesador')
        camara = data.get('camara')
        bateria = data.get('bateria')
        pantalla = data.get('pantalla')
        memoria = data.get('memoria')

        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, imagen=imagen, categoria_id=categoria_id, modelo_id=modelo_id, almacenamiento_id=almacenamiento_id, color_id=color_id, stock=stock, procesador=procesador, camara=camara, bateria=bateria, pantalla=pantalla, memoria=memoria)

        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'message': 'Producto agregado correctamente'}), 201
    
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error al agregar el producto'}), 500