from model.user import User
from misc.utility_functions import *

class Hospital(User):

    __ID = 0

    def __init__(self, system):
        self.id = Hospital.__ID
        self.system = system
        Hospital.__ID += 1

    def request_blood(self):
        blood_type = type_to_int(input('Enter blood type (A|B|AB|O)[+-]: '))
        amount = int(input('Enter amount: '))
        if self.system.request_blood(self.id, blood_type, amount):
            print('Request accepted.')
        else:
            print('Request rejected.')
    
    def print_instructions(self):
        print(
'''
----------------------------------------------------------------
This system supports the following commands for Hospitals:
----------------------------------------------------------------
| request blood  | request blood deposit from system           |
----------------------------------------------------------------
| help           | print all available commands                |
----------------------------------------------------------------
'''
        )