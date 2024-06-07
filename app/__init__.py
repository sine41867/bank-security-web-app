from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.models.database_handler import DatabaseHandler
from app.routes.admin_routes import admin_bp
from app.routes.officer_routes import officer_bp
from app.routes.common_routes import common_bp

bcrypt = Bcrypt()
login_manager = LoginManager()

login_manager.login_view = 'common_bp.login'
login_manager.session_protection = "strong"




def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(officer_bp, url_prefix='/officer')
    app.register_blueprint(common_bp)
    return app


@login_manager.user_loader
def load_user(user_id):
    dbHandler = DatabaseHandler()
    return dbHandler.load_user(user_id)

