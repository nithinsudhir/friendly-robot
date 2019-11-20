from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor
from misc.utility_functions import *
from misc.messages import *
import re

def login(current_user):
    if current_user == 'A':
        return Administrator(system)
    elif current_user == 'H':
        return Hospital(system)
    elif current_user == 'D':
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        age = int(input('Enter age: '))
        blood_type = input('Enter blood type (A|B|AB|O)[+-]: ')
        email = input('Enter email: ')
        allergens = input('Enter allergens (if applicable): ')
        return Donor(system, first_name, last_name, age, blood_type, email, allergens)
    else:
        print('Invalid user. Please try again')
        current_user = input('Please enter your user type (A/H/D): ')
        user = login(current_user)
        return user

if __name__ == '__main__':

    print(WELCOME_MESSAGE)
    system = System()
    current_user = input('Please enter your user type (A/H/D): ')
    user = login(current_user)
    print('Logged in as ' + user.get_type())
    user.print_instructions()
    user.warn_scarce_blood_types()

    while True:

        action = input('Enter a command: ')

        if action == 'help':
            user.print_instructions()
        
        elif action == 'count':
            user.count_deposits()
        
        elif action == 'volume':
            user.count_volume()

        elif action == 'add deposit':
            user.add_deposit()

        elif action == 'remove deposit':
            user.remove_deposit()
        
        elif action == 'filter':
            user.filter_blood()

        elif action == 'add donor':
            user.add_donor()
        
        elif action == 'remove donor':
            user.remove_donor()

        elif action == 'request blood':
            user.request_blood()
        
        elif action == 'register':
            user.register()
        
        elif action == 'donate':
            user.donate_blood()

        elif action == 'sort blood':
            user.sort_by_expiry()

        else:
            print('Command not recognised, please try again')
            continue
