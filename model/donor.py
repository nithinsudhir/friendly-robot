from model.user import User

class Donor(User):
    def __init__(self, system, first_name, last_name, age, blood_type, email, allergens):
        self.system = system
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.blood_type = blood_type
        self.email = email
        self.allergens = allergens
        self.is_elligible = self.get_eligibility()

    def get_eligibility(self):
        return True if self.age < 75 and self.allergens is '' else False
    
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
