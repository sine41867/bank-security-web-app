from flask import redirect, url_for,  flash
from flask_login import current_user
from functools import wraps
from app.models.messages import Messages

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 1:
            flash(Messages.invalid_access, category='danger')
            return redirect(url_for('common_bp.login'))
        return f(*args, **kwargs)
    return decorated_function

def officer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 0:
            flash(Messages.invalid_access, category='danger')
            return redirect(url_for('common_bp.login'))
        return f(*args, **kwargs)
    return decorated_function
