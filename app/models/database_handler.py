import pymysql
from flask import flash
from app.models.user import User

class DatabaseHandler:
  
    def __init__(self):
        self.db_host = "127.0.0.1"
        self.db_user = "root"
        self.db_password = ""
        self.db_name = "db_security_system"
    
    def connection(self):
        try:
            conn = pymysql.connect(host= self.db_host, user = self.db_user, password= self.db_password, database= self.db_name)
            return conn
        except Exception as e:
            flash(str(e), category='danger')        
    
    def isUser(self,conn, user_id):
        try:
            query = "SELECT * FROM tbl_users WHERE user_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()      

            if result:
                return True
            else:
                return False
        except Exception as e:
            flash(str({e}), category='danger')
    
    def isRobber(self, conn, robber_id):
        try:
            query = "SELECT * FROM tbl_robbers WHERE robber_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, (robber_id,))
            result = cursor.fetchone()      

            if result:
                return True
            else:
                return False
        except Exception as e:
            flash(str({e}), category='danger')
    
    def isBlacklisted(self, conn, cif_no):
        try:
            query = "SELECT * FROM tbl_blacklisted WHERE cif_no=%s"
            cursor = conn.cursor()
            cursor.execute(query, (cif_no,))
            result = cursor.fetchone()      

            if result:
                return True
            else:
                return False
        except Exception as e:
            flash(str({e}), category='danger')

    def load_user(self, user_id):
        conn = self.connection()
        if not conn :
            return
        
        try:
            query = "SELECT * FROM tbl_users WHERE user_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                user = User(result[0], result[2],result[3], result[4], result[5])
                return user        
            return None
    
        except Exception as e:
            flash(str({e}), category='danger')
            
    def check_credential(self, user_id, password):
        conn = self.connection()
        if not conn :
            return
        
        try:
            query = "SELECT * FROM tbl_users WHERE user_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            conn.close()

            if result and (result[5] > 2):
                flash('Your Account is deactivated.', category='danger')
                return None

            if result:
                from app import bcrypt
                
                isPasswordValid = bcrypt.check_password_hash(result[1],password)
                
                if isPasswordValid:
                    self.set_invalid_attempts(user_id,-1)
                    user = User(result[0], result[2],result[3], result[4], None, result[5])
                    return user
                else:
                    self.set_invalid_attempts(user_id, result[5])
                    flash("Invalid Passoword", category='danger')
                    return None
            else:
                flash('Invalid User ID', category='danger')
                return None
                  
        except Exception as e:
            flash(str({e}), category='danger')
                    
    def set_invalid_attempts(self, user_id, current_attempts):
        conn = self.connection()
        if not conn :
            return
        
        try:
            query = "UPDATE tbl_users SET invalid_attempts = '%s' WHERE user_id = %s"
            data = ((current_attempts + 1), user_id,)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

        except Exception as e:
            flash(str({e}), category='danger')

    def insert_user(self, user):
        conn = self.connection()
        if not conn :
            return
        
        try:
            query = "INSERT INTO tbl_users (user_id, password, type, inserted_by, time, invalid_attempts) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (user.user_id, user.password, user.user_type, user.inserted_by,user.time,user.invalid_attempts)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            flash('Inserted...', category='success')
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def insert_blacklisted_customer(self, blacklisted_customer):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            query = "INSERT INTO tbl_blacklisted (cif_no, photo, description, inserted_by, time) VALUES (%s, %s, %s, %s, %s)"
            data = (blacklisted_customer.cif_no, blacklisted_customer.photo_path, blacklisted_customer.description, blacklisted_customer.inserted_by, blacklisted_customer.time)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            flash('Inserted...', category='success')
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def insert_robber(self, robber):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            query = "INSERT INTO tbl_robbers (robber_id, name, photo, description, inserted_by, time) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (robber.robber_id, robber.name, robber.photo_path, robber.description, robber.inserted_by,robber.time,)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            flash('Inserted...', category='success')
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def get_all_blacklisted_customers(self, search_text):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            cursor = conn.cursor()
            if search_text:
                query = "SELECT cif_no, description, inserted_by, time FROM tbl_blacklisted WHERE cif_no LIKE %s OR description LIKE %s OR time LIKE %s"
                data = ('%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%')
                cursor.execute(query, data)
                
            else:
                query = "SELECT cif_no, description, inserted_by, time FROM tbl_blacklisted"
                cursor.execute(query)
            
            blacklisted_customers = cursor.fetchall()
            conn.close()

            return blacklisted_customers
                  
        except Exception as e:
            flash(str({e}), category='danger')
    
    def get_blacklisted_customer(self, cif_no):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            query = "SELECT * FROM tbl_blacklisted WHERE cif_no=%s"
            cursor = conn.cursor()
            cursor.execute(query, cif_no)
            blacklisted_customer = cursor.fetchone()
            conn.close()

            return blacklisted_customer
                  
        except Exception as e:
            flash(str({e}), category='danger')
    
    def get_all_robbers(self, search_text):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            cursor = conn.cursor()
            if search_text:
                query = "SELECT robber_id, name, description, inserted_by, time FROM tbl_robbers WHERE robber_id LIKE %s OR description LIKE %s OR name LIKE %s OR time LIKE %s"
                data = ('%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%')
                cursor.execute(query, data)
                
            else:
                query = "SELECT robber_id, name, description, inserted_by, time FROM tbl_robbers"
                cursor.execute(query)
            
            robber = cursor.fetchall()
            conn.close()

            return robber
                  
        except Exception as e:
            flash(str({e}), category='danger')
    
    def get_robber(self, robber_id):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            query = "SELECT * FROM tbl_robbers WHERE robber_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, robber_id)
            robber = cursor.fetchone()
            conn.close()

            return robber
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def delete_blacklisted_customer(self, cif_no):
        conn = self.connection()
        if not conn :
            return
        
        try:
            if not self.isBlacklisted(conn, cif_no):
                flash('Invalid CIF Number...', category='danger')
                conn.close()
                return
            
            query = "DELETE FROM tbl_blacklisted WHERE cif_no = %s"
            cursor = conn.cursor()
            cursor.execute(query, cif_no)
            conn.commit()
            conn.close()

            flash('Deleted...', category='success')
             
        except Exception as e:
            flash(str({e}), category='danger')

    def delete_robber(self, robber_id):
        conn = self.connection()
        if not conn :
            return
        
        try:
            if not self.isRobber(conn, robber_id):
                flash('Invalid Robber ID...', category='danger')
                conn.close()
                return
            
            query = "DELETE FROM tbl_robbers WHERE robber_id = %s"
            cursor = conn.cursor()
            cursor.execute(query, robber_id)
            conn.commit()
            conn.close()

            flash('Deleted...', category='success')
             
        except Exception as e:
            flash(str({e}), category='danger')

    def reset_password(self, user):
        conn = self.connection()
        if not conn :
            return
        
        try:
            if not self.isUser(conn, user.user_id):
                flash('Invalid User ID...', category='danger')
                conn.close()
                return
                
            query = "UPDATE tbl_users SET password = %s WHERE user_id = %s"
            data = (user.password, user.user_id,)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            flash('Resetted...', category='success')
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def activate_account(self, user_id):
        conn = self.connection()
        if not conn :
            return
        
        try:
            if not self.isUser(conn, user_id):
                flash('Invalid User ID...', category='danger')
                conn.close()
                return
                
            query = "UPDATE tbl_users SET invalid_attempts = '%s' WHERE user_id = %s"
            data = (0, user_id,)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            conn.close()

            flash('Acivated...', category='success')
                  
        except Exception as e:
            flash(str({e}), category='danger')

    def delete_user(self, user_id):
        conn = self.connection()
        if not conn :
            return
        
        try:
            if not self.isUser(conn, user_id):
                flash('Invalid User ID...', category='danger')
                conn.close()
                return

            query = "DELETE FROM tbl_users WHERE user_id = %s"
            cursor = conn.cursor()
            cursor.execute(query, user_id)
            conn.commit()
            conn.close()

            flash('Deleted...', category='success')
             
        except Exception as e:
            flash(str({e}), category='danger')
            
    def get_all_alerts(self, search_text):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            cursor = conn.cursor()
            if search_text:
                query = "SELECT alert_id, type, description, time, branch_id, generated_by FROM tbl_alerts WHERE alert_id LIKE %s OR type LIKE %s OR time LIKE %s OR description LIKE %s OR branch_id LIKE %s OR generated_by LIKE %s ORDER BY alert_id DESC"
                data = ('%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%')
                cursor.execute(query, data)
                
            else:
                query = "SELECT alert_id, type, description, time, branch_id, generated_by FROM tbl_alerts ORDER BY alert_id DESC"
                cursor.execute(query)
            
            alerts = cursor.fetchall()
            conn.close()

            return alerts
                  
        except Exception as e:
            flash(str({e}), category='danger')
    
    def get_alert(self, alert_id):
        conn = self.connection()
        
        if not conn :
            return
        
        try:
            query = "SELECT * FROM tbl_alerts WHERE alert_id=%s"
            cursor = conn.cursor()
            cursor.execute(query, alert_id)
            alert = cursor.fetchone()
            conn.close()

            return alert
                  
        except Exception as e:
            flash(str({e}), category='danger')
    
    #for testing purpose
    def test(self):
        from app import bcrypt
        hashed_password = bcrypt.generate_password_hash("pass").decode('utf-8')
        user_id = "00000"

        query2 = "UPDATE tbl_users SET password = %s WHERE user_id = %s"

        conn = self.connection()
        conn.cursor().execute(query2,(hashed_password, user_id))
        conn.commit()
        conn.close()

        return "OK"
               