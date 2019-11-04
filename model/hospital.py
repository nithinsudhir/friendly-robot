from .user import User

class Hospital(User):
    def __init__(self, hospital_args = None):
        self.hospital_args = hospital_args
        self.user_type = 'Hospital'
