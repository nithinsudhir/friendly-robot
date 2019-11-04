from .user import User

class Administrator(User):
    def __init__(self, administrator_args = None):
        self.administrator_args = administrator_args
        self.user_type = 'Administrator'