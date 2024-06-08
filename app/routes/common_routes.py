from flask import request, redirect, url_for, render_template, flash, jsonify, Blueprint
from flask_login import login_required, logout_user, login_user
import base64
from app.models.database_handler import DatabaseHandler
#from app import bcrypt


common_bp = Blueprint('common_bp', __name__)
dbHandler = DatabaseHandler()

#for testing purpose
@common_bp.route('/test')
def test():
    return dbHandler.test()
    #return "Test Success"
    return render_template('test.html')

@common_bp.route('/', methods=['GET', 'POST'])
def login():
    logout_user()
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

        dbHandler = DatabaseHandler()
        
        user = dbHandler.check_credential(user_id=user_id, password= password)

        if user :
            login_user(user)

            next = request.args.get('next')

            if next and next[1:6]=="admin":
                next = "admin_bp." + next[7:]
            elif next and next[1:8] == "officer":
                next = "officer_bp." + next[9:]
            elif next:
                next = "common_bp." + next[1:]

            if user.user_type == 0:
                return redirect(url_for(next or 'officer_bp.home'))
            
            if user.user_type == 1:
                return redirect(url_for(next or 'admin_bp.home'))
        else:
            return redirect(url_for('common_bp.login'))
        
    return render_template('common/login.html')

@common_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('common_bp.login'))

@common_bp.route('/view_blacklisted_customers')
@login_required
def view_blacklisted_customers():

    dbHandler = DatabaseHandler()
    customers = dbHandler.get_all_blacklisted_customers(None)

    return render_template('common/view_blacklisted_customers.html', customers = customers)

@common_bp.route('/view_robbers')
@login_required
def view_robbers():
    
    dbHandler = DatabaseHandler()
    robbers = dbHandler.get_all_robbers(None)

    return render_template('common/view_robbers.html', robbers=robbers)

@common_bp.route('/blacklisted_customer/<cif_no>')
@login_required
def blacklisted_customer_details(cif_no):
    
    dbHandler = DatabaseHandler()
    customer = dbHandler.get_blacklisted_customer(cif_no)
    if customer:
        photo_base64 = base64.b64encode(customer[1]).decode('utf-8')
        return render_template('common/blacklisted_customer_details.html', customer=customer, photo_base64=photo_base64)
    else:
        flash('Blacklisted Customer not found', category='danger')
        return redirect(url_for('common_bp.view_blacklisted_customers'))

@common_bp.route('/robber/<robber_id>')
@login_required
def robber_details(robber_id):
    
    dbHandler = DatabaseHandler()
    robber = dbHandler.get_robber(robber_id)
    if robber:
        photo_base64 = base64.b64encode(robber[2]).decode('utf-8')
        return render_template('common/robber_details.html', robber=robber, photo_base64=photo_base64)
    else:
        flash('Robber not found', category='danger')
        return redirect(url_for('common_bp.view_robbers'))

@common_bp.route('/search_blacklisted', methods = ['GET'])
@login_required
def search_blacklisted():
    search_text = request.args.get('search_text', '')

    dbHandler = DatabaseHandler()
    blacklisted_customers = dbHandler.get_all_blacklisted_customers(search_text)

    return jsonify(blacklisted_customers)

@common_bp.route('/search_robber', methods = ['GET'])
@login_required
def search_robbers():
    search_text = request.args.get('search_text', '')

    dbHandler = DatabaseHandler()
    robber = dbHandler.get_all_robbers(search_text)

    return jsonify(robber)


#-------------------------------------------------------------------
@common_bp.route('/view_alerts')
@login_required
def view_alerts():

    dbHandler = DatabaseHandler()
    alerts = dbHandler.get_all_alerts(None)

    return render_template('common/view_alerts.html', alerts = alerts)

@common_bp.route('/alert/<alert_id>')
@login_required
def alert_details(alert_id):
    
    dbHandler = DatabaseHandler()
    alert = dbHandler.get_alert(alert_id)
    if alert:
        photo_base64 = base64.b64encode(alert[3]).decode('utf-8')
        return render_template('common/alert_details.html', alert=alert, photo_base64=photo_base64)
    else:
        flash('Alert not found', category='danger')
        return redirect(url_for('common_bp.view_alerts'))

@common_bp.route('/search_alert', methods = ['GET'])
@login_required
def search_alert():
    search_text = request.args.get('search_text', '')

    dbHandler = DatabaseHandler()
    alerts = dbHandler.get_all_alerts(search_text)

    return jsonify(alerts)
