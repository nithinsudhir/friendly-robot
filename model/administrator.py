from model.user import User

class Administrator(User):
    def __init__(self, system):
        self.system = system
        self.user_type = 'Administrator'

    def add_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.add_blood_deposit(self, blood_type, is_valid, expiry_date, amount)

    def remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount):
        self.system.remove_blood_deposit(self, blood_type, is_valid, expiry_date, amount)

    def print_instructions(self):
        print('This system accepts the following commands:')
        print('count - count number of blood deposits')
        print('volume - count total volume of blood deposits')
        print('help - print all available commands\n\n')