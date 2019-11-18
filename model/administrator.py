from model.user import User
from misc.utility_functions import *
import re

class Administrator(User):
    def __init__(self, system):
        self.system = system
        
    def add_donor(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        blood_type = type_to_int(input("Enter blood type (A|B|AB|O)[+-]: "))
        email = input("Enter email: ")
        allergens = input("Enter allergens (N/A if none): ")
        self.system.add_donor(first_name, last_name, age, blood_type, email, allergens)
        print("Donor added succesfully")
    
    def remove_donor(self):
        donor_id = int(input('Enter donor ID: '))
        self.system.remove_donor(donor_id)
        print('Donor removed successfully')


    def count_deposits(self):
        option = input('Enter (A|B|AB|O)[+-] to specify type [optional]: ')
        if not option:
            print(self.system.count_deposits())
        elif re.match(r'^(A|B|AB|O)[+-]$', option):
            blood_type = type_to_int(option)
            print(self.system.count_deposits(blood_type))
        else:
            print('Unrecognised blood type, please try again.')
            self.count_deposits()

    def warn_scarce_blood_types(self):
        blood_total_lower_limit = 500
        scarce = self.system.get_scarce_blood_types(blood_total_lower_limit)
        if (scarce != []):
            print_scarce_blood(scarce)

    def count_volume(self):
        option = input('Enter (A|B|AB|O)[+-] to specify type [optional]: ')
        if not option:
            print(self.system.count_volume())
        elif re.match(r'^(A|B|AB|O)[+-]$', option):
            blood_type = type_to_int(option)
            print(self.system.count_volume(blood_type))
        else:
            print('Unrecognised blood type, please try again.')
            self.count_volume()
    
    def add_deposit(self):
        donor_id = int(input('Enter donor ID: '))
        blood_type = type_to_int(input('Enter blood type (A|B|AB|O)[+-]: '))
        expiry_date = date_to_int(input('Enter expiry date (dd/mm/yyyy): '))
        amount = int(input('Enter amount: '))
        self.system.add_deposit(donor_id, blood_type, expiry_date, amount)
        print('Deposit added successfully')

    def remove_deposit(self):
        deposit_id = int(input('Enter deposit ID: '))
        self.system.remove_deposit(deposit_id)
        print('Deposit removed successfully')

    def filter_blood(self):
        filter_attribute = input('Enter (Type | Amount) to specify filter attribute: ')
        if re.match(r'^(Type|Amount)$', filter_attribute):
            attribute = attribute_to_int(filter_attribute)
            if (filter_attribute == 'Type'):
                option = input('Enter (A|B|AB|O)[+-] to specify blood type: ')
                if re.match(r'^(A|B|AB|O)[+-]$', option):
                    value = type_to_int(option)
                    filtered = self.system.filter_by_attribute(attribute,value)
                    display_results(filtered)
                else:
                    print('Unrecognised blood type, please try again.')
                    self.filter_blood()
            elif (filter_attribute == 'Amount'):
                option = input('Enter amount to filter deposits by: ')
                if re.match(r'^[0-9]+$', option):
                    value = int(option)
                    filtered = self.system.filter_by_attribute(attribute,value)
                    display_results(filtered)
                else:
                    print('Unrecognised amount, please enter a number and try again.')
                    self.filter_blood()
        else:
            print('Unrecognised blood type, please try again.')
            self.filter_blood()

    def print_instructions(self):
        print(
'''
----------------------------------------------------------------
This system supports the following commands for Administrators:
----------------------------------------------------------------
| count          | count number of blood deposits              |
----------------------------------------------------------------
| volume         | count total volume of blood deposits        |
----------------------------------------------------------------
| add deposit    | add blood deposit to system                 |
----------------------------------------------------------------
| remove deposit | remove blood deposit from system            |
----------------------------------------------------------------
| add donor      | add donor record to the system              |
----------------------------------------------------------------
| remove donor   | remove donor record from the system         |
----------------------------------------------------------------
| help           | print all available commands                |
----------------------------------------------------------------
'''
        )
    
