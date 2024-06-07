from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, status, user_type, inserted_by,time, password=None):
        self.user_id = user_id
        self.status = status
        self.user_type = user_type
        self.inserted_by = inserted_by
        self.time = time
        self.password = password
            
    def get_id(self):
        return self.user_id
