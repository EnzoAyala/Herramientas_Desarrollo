from flask import Flask, render_template
from config import Config
from models import db, seed_data

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa SQLAlchemy con la app
    db.init_app(app)

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

    return app

# Ejecuta la app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)