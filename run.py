from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor
from utility_functions import type_to_int
import re

def login(current_user):
    if current_user == 'A':
        return Administrator(system)
    elif current_user == 'H':
        return Hospital(system)
    elif current_user == 'D':
        return Donor(system)
    else:
        print('Invalid user. Please try again')
        current_user = input('Please enter your user type (A/H/D): ')
        user = login(current_user)
        return user

def print_instructions():
    print('This system accepts the following commands:')
    print('count - count number of blood deposits')
    print('volume - count total volume of blood deposits')
    print('help - print all available commands\n\n')

def handle_count():
    option = input('Enter (A|B|AB|O) to specify type [optional]: ')
    if not option:
        print(system.count_deposits())
    elif re.match(r'^(A|B|AB|O)$', option):
        blood_type = type_to_int(option)
        print(system.count_deposits(blood_type))
    else:
        print('Unrecognised blood type, please try again.')
        handle_count()

def handle_volume():
    option = input('Enter (A|B|AB|O) to specify type [optional]: ')
    if not option:
        print(system.count_volume())
    elif re.match(r'^(A|B|AB|O)$', option):
        blood_type = type_to_int(option)
        print(system.count_volume(blood_type))
    else:
        print('Unrecognised blood type, please try again.')
        handle_volume()

def handle_add():
    pass

def handle_remove():
    pass

print('Welcome to the DafnyDuk Blood Managment System\n')

print('Initialising system...\n')
system = System()
print('System initialised successfully.\n')

print('This system accepts three different types of users:')
print('A - Administrator')
print('H - Hospital')
print('D - Donor\n\n')
current_user = input('Please enter your user type (A/H/D): ')
user = login(current_user)

print('Logged in as '+ str(user.get_user_type()))

print_instructions()

while True:

    action = input('Enter a command: ')

    if action == 'help':
        print_instructions()
    
    elif action == 'count':
        handle_count()
    
    elif action == 'volume':
        handle_volume()

    elif action == 'add':
        handle_count()

    elif action == 'remove':
        handle_remove()
    
    else:
        print('Command not recognised, please try again')
        continue
