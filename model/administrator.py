from model.user import User

class Administrator(User):
    def __init__(self, system):
        self.system = system
        self.user_type = 'Administrator'

    def add_deposit(self, donor_id, blood_type, expiry_date, amount):
        self.system.add_deposit(donor_id, blood_type, expiry_date, amount)

    def remove_deposit(self, deposit_id):
        self.system.remove_deposit(deposit_id)

    def add_donor(self, first_name, last_name, age, blood_type, email, allergens):
        self.system.add_donor(self, first_name, last_name, age, blood_type, email, allergens)

    def remove_donor(self, donor_id):
        self.system.remove_donor(donor_id)