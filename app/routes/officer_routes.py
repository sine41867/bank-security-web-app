from flask import render_template, Blueprint, Response
from flask_login import login_required
from app.models.database_handler import DatabaseHandler
from app.utils.decorators import officer_required
from app.models.camera_handler import CameraHandler


officer_bp = Blueprint('officer_bp', __name__)
dbHandler = DatabaseHandler()
camera_handler = CameraHandler()

@officer_bp.route('/home')
@login_required
@officer_required
def home():
    return render_template('officer/home.html')

@officer_bp.route('/live_footages')
#@login_required
#@officer_required
def live_footages():
    return render_template('officer/home.html')

@officer_bp.route('/video_feed')
def video_feed():
    return Response(camera_handler.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

