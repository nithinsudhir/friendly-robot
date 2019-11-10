from model.user import User

class Hospital(User):

    __ID = 0

    def __init__(self, system):
        self.id = Hospital.__ID
        self.system = system
        self.user_type = 'Hospital'
        Hospital.__ID += 1

    def request_blood(self, blood_type, amount):
        return self.system.request_blood(self.id, blood_type, amount)
