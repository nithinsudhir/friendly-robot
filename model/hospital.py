from model.user import User

class Hospital(User):
    def __init__(self, system):
        self.system = system
        self.user_type = 'Hospital'
