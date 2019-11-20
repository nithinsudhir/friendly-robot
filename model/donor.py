from model.user import User
from misc.utility_functions import date_to_int, type_to_int

class Donor(User):
    def __init__(self, system, first_name, last_name, age, blood_type, email, allergens):
        self.system = system
        self.id = max(system.donors)[0] + 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.blood_type = type_to_int(blood_type)
        self.email = email
        self.allergens = allergens
        self.is_elligible = self.get_eligibility()

    def get_eligibility(self):
        return True if self.age < 75 and self.allergens is '' else False
    
    def register(self):
        self.system.add_donor(self.first_name, self.last_name, self.age, self.blood_type, self.email, self.allergens)

    def donate_blood(self):
        amount = input('Enter amount (mL): ')
        expiry_date = date_to_int(input('Enter expiry date (dd/mm/yyyy): '))
        self.system.add_deposit(self.id, self.blood_type, expiry_date, amount)

    def print_instructions(self):
        print(
'''
----------------------------------------------------------------
This system supports the following commands for Donors:
----------------------------------------------------------------
| register   | register as donor in system                     |
----------------------------------------------------------------
| donate     | donate blood deposit                            |
----------------------------------------------------------------
| help       | print all available commands                    |
----------------------------------------------------------------
        '''
        )