from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

def hash_password(password):
    return generate_password_hash(password)

def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not hasattr(current_user, 'rol') or current_user.rol.name != 'administrador':
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
