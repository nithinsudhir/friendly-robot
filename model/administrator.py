from .user import User


class Administrator(User):
    def __init__(self, system = None):
        self.system = system
        self.user_type = 'Administrator'

    def add_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.add_blood_deposit(self, blood_type, is_valid, expiry_date, amount)

    def remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount)

    def add_donor(self, first_name, last_name, age, email, phone, blood_type, allergens):
        self.system.add_donor(self, first_name, last_name, age, email, phone, blood_type, allergens)


    def get_user_type(self):
        return self.user_type