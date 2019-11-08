from model.user import User

class Administrator(User):
    def __init__(self, system):
        self.system = system
        self.user_type = 'Administrator'

    def add_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.add_blood_deposit(self, blood_type, is_valid, expiry_date, amount)

    def remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount)