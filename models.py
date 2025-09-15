from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definición de modelos (tablas)

class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    dni = db.Column(db.String(20), unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=1)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.Text)
    productos = db.relationship('Producto', backref='categoria', lazy=True)

class Modelo(db.Model):
    __tablename__ = 'modelos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    productos = db.relationship('Producto', backref='modelo', lazy=True)

class Almacenamiento(db.Model):
    __tablename__ = 'almacenamientos'
    id = db.Column(db.Integer, primary_key=True)
    capacidad = db.Column(db.String(50), nullable=False)
    productos = db.relationship('Producto', backref='almacenamiento', lazy=True)

class Color(db.Model):
    __tablename__ = 'colores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    productos = db.relationship('Producto', backref='color', lazy=True)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2))
    imagen = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelos.id'))
    almacenamiento_id = db.Column(db.Integer, db.ForeignKey('almacenamientos.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colores.id'))
    stock = db.Column(db.Integer)


def seed_data():
    from models import Rol, Almacenamiento, db

    # Inicializar roles
    if not Rol.query.first():
        roles = [Rol(name='usuario'), Rol(name='administrador')]
        db.session.add_all(roles)
        print('Roles insertados')

    # Inicializar almacenamientos
    if not Almacenamiento.query.first():
        almacenamientos = [
            Almacenamiento(capacidad='128GB'),
            Almacenamiento(capacidad='256GB'),
            Almacenamiento(capacidad='1TB'),
        ]
        db.session.add_all(almacenamientos)
        print('Almacenamientos insertados')

    db.session.commit()