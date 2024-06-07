from flask import render_template, Blueprint
from flask_login import login_required
from app.models.database_handler import DatabaseHandler
from app.utils.decorators import officer_required


officer_bp = Blueprint('officer_bp', __name__)
dbHandler = DatabaseHandler()

@officer_bp.route('/home')
@login_required
@officer_required
def officer_home():
    return render_template('officer/home.html')

