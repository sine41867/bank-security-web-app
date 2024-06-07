from flask import redirect, url_for,  flash
from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 1:
            flash('You do not have permission to access this page.', category='danger')
            return redirect(url_for('common_bp.login'))
        return f(*args, **kwargs)
    return decorated_function

def officer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 0:
            flash('You do not have permission to access this page.', category='danger')
            return redirect(url_for('common_bp.login'))
        return f(*args, **kwargs)
    return decorated_function
