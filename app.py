from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Rol, Almacenamiento, Usuario
from security import hash_password, check_password
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

def seed_data():
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

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'super-secret-key'  # Necesario para flash messages

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
        seed_data()

    # RUTAS
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/catalogo')
    def catalogo():
        return render_template('catalogo.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if request.method == 'POST':
            correo = request.form['correo']
            contrasena = request.form['contrasena']
            usuario = Usuario.query.filter_by(correo=correo).first()

            if usuario and check_password(usuario.contrasena, contrasena):
                login_user(usuario)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('index'))
            else:
                flash('Credenciales inválidas. Por favor, inténtalo de nuevo.', 'danger')
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
            
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            correo = request.form['correo']
            telefono = request.form['telefono']
            dni = request.form['dni']
            contrasena = request.form['contrasena']

            # Validar que el correo no exista
            if Usuario.query.filter_by(correo=correo).first():
                flash('El correo ya está registrado.', 'danger')
                return redirect(url_for('register'))
            
            # Validar que el DNI sea unico
            if Usuario.query.filter_by(dni=dni).first():
                flash('El DNI ya está registrado.', 'danger')
                return redirect(url_for('register'))

            hashed_password = hash_password(contrasena)
            
            nuevo_usuario = Usuario(
                nombre=nombre, 
                apellido=apellido, 
                correo=correo, 
                telefono=telefono, 
                dni=dni, 
                contrasena=hashed_password
            )
            
            db.session.add(nuevo_usuario)
            db.session.commit()

            flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html')


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Has cerrado sesión exitosamente.', 'info')
        return redirect(url_for('index'))


    return app

# Ejecuta la app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)