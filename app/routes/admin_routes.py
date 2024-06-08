from flask import request, redirect, url_for, render_template, flash, Blueprint, make_response
from flask_login import login_required, current_user
from app.models.database_handler import DatabaseHandler
from app.models.blacklisted_customer import BlacklistedCustomer
from app.models.user import User
from app.models.robber import Robber
from app.utils.file_utils import allowed_file
from app.utils.decorators import admin_required
from datetime import datetime

admin_bp = Blueprint('admin_bp', __name__)
dbHandler = DatabaseHandler()

@admin_bp.route('/home')
@login_required
@admin_required
def home():
    return render_template('admin/home.html')

@admin_bp.route('/users')
@admin_required
@login_required
def users():
    return render_template('admin/users.html')

@admin_bp.route('/blacklisted_customers')
@login_required
@admin_required
def blacklisted_customers():
    return render_template('admin/blacklisted_customers.html')

@admin_bp.route('/robbers')
@login_required
@admin_required
def robbers():
    return render_template('admin/robbers.html')

@admin_bp.route('/delete_blacklisted_customers', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_blacklisted_customer():
    if request.method == 'POST':
        cif_no = request.form['cif_no']
                
        dbHandler.delete_blacklisted_customer(cif_no)

        return redirect(url_for('admin_bp.delete_blacklisted_customer'))

    return render_template('admin/delete_blacklisted_customer.html')

@admin_bp.route('/insert_blacklisted_customer', methods=['GET', 'POST'])
@login_required
@admin_required
def insert_blacklisted_customer():
    if request.method == 'POST':
        cif_no = request.form['cif_no']
        description = request.form['description']
        file = request.files['image']
        
        
        # Handle the image file
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        

        if file and allowed_file(file.filename):
            photo = file.read()

            time_stamp = datetime.now()

            blacklisted_customer = BlacklistedCustomer(
                cif_no=cif_no,
                photo_path=photo,
                description=description,
                inserted_by=current_user.user_id,
                time=time_stamp
            )

            dbHandler.insert_blacklisted_customer(blacklisted_customer)

            return redirect(url_for('admin_bp.insert_blacklisted_customer'))

    return render_template('admin/insert_blacklisted_customer.html')

@admin_bp.route('/create_account', methods=['GET', 'POST'])
@login_required
@admin_required
def create_account():
    from app import bcrypt
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_type = request.form['user_type']
        password = request.form['password']
        time_stamp = datetime.now()

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        user = User(user_id,user_type,current_user.user_id,time_stamp,hashed_password)
        

        dbHandler.insert_user(user)

        return redirect(url_for('admin_bp.create_account'))

    return render_template('admin/create_account.html')

@admin_bp.route('/activate_account', methods=['GET', 'POST'])
@login_required
@admin_required
def activate_account():

    if request.method == 'POST':
        
        user_id = request.form['user_id']
        
        dbHandler.activate_account(user_id)

        return redirect(url_for('admin_bp.activate_account'))

    return render_template('admin/activate_account.html')

@admin_bp.route('/delete_account', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_account():

    if request.method == 'POST':
        user_id = request.form['user_id']
                
        dbHandler.delete_user(user_id)

        return redirect(url_for('admin_bp.delete_account'))

    return render_template('admin/delete_account.html')

@admin_bp.route('/reset_password', methods=['GET', 'POST'])
@login_required
@admin_required
def reset_password():
    from app import bcrypt
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
    
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
        user = User(user_id,None,None,None,hashed_password)  

        dbHandler.reset_password(user)

        return redirect(url_for('admin_bp.reset_password'))

    return render_template('admin/reset_password.html')

@admin_bp.route('/delete_robber', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_robber():
    if request.method == 'POST':
        robber_id = request.form['robber_id']
                
        dbHandler.delete_robber(robber_id)

        return redirect(url_for('admin_bp.delete_robber'))

    return render_template('admin/delete_robber.html')

@admin_bp.route('/insert_robbers', methods=['GET', 'POST'])
@login_required
@admin_required
def insert_robber():

    if request.method == 'POST':
        robber_id = request.form['robber_id']
        name = request.form['name']
        description = request.form['description']
        file = request.files['image']
        
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        

        if file and allowed_file(file.filename):
            photo = file.read()

            time_stamp = datetime.now()
            robber = Robber(
                robber_id=robber_id,
                name=name,
                photo_path=photo,
                description=description,
                inserted_by=current_user.user_id,
                time=time_stamp
            )

            dbHandler.insert_robber(robber)

            return redirect(url_for('admin_bp.insert_robber'))

    return render_template('admin/insert_robber.html')
