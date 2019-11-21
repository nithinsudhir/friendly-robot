from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor
from misc.utility_functions import *
from misc.messages import *
import re

def login(current_user):
    current_user = current_user.lower()
    if current_user == 'a':
        return Administrator(system)
    elif current_user == 'h':
        return Hospital(system)
    elif current_user == 'd':
        print_donor_prompt()
        option = input('Enter option: ')
        if option == 'register':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            age = int(input('Enter age: '))
            blood_type = input('Enter blood type (A|B|AB|O)[+-]: ')
            email = input('Enter email: ')
            allergens = input('Enter allergens (N/A if none): ')
            donor = Donor(system, first_name, last_name, age, blood_type, email, allergens)
            donor.register()
        elif option == 'login':
            email = input('Enter email address: ')
            donor = system.get_donor_by_email(email)
            if donor:
                first_name = donor[1]
                last_name = donor[2]
                age = int(donor[3])
                blood_type = int(donor[4])
                email = donor[5]
                allergens = donor[6]
                donor = Donor(system, first_name, last_name, age, blood_type, email, allergens)
            else:
                print(f'No record of donor with email address {email}. Please try again.')
                current_user = input('Please enter your user type (A/H/D): ')
                user = login(current_user)
        return donor
    else:
        print('Invalid user. Please try again')
        current_user = input('Please enter your user type (A/H/D): ')
        user = login(current_user)
        return user

def print_donor_prompt():
    print(
'''
----------------------------------------------------------------
Please choose an option:
----------------------------------------------------------------
| login      | login as an existing donor                      |
----------------------------------------------------------------
| register   | register as a donor                             |
----------------------------------------------------------------
'''
)

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

        elif action == 'logout':
            print(type(user).__name__+ " logging out")
            exit()

        else:
            print('Command not recognised, please try again')
            continue
