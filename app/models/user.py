from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, user_type, inserted_by,time, password=None, invalid_attempts=0):
        self.user_id = user_id
        self.user_type = user_type
        self.inserted_by = inserted_by
        self.time = time
        self.password = password
        self.invalid_attempts = invalid_attempts
            
    def get_id(self):
        return self.user_id
