from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor
from misc.utility_functions import *
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
    filtered = get_filter_input()
    print(len(filtered))

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

def get_filter_input():
    filter_attribute = input('Enter (Type | Amount) to specify filter attribute: ')
    if re.match(r'^(Type|Amount)$', filter_attribute):
        attribute = attribute_to_int(filter_attribute)
        if (filter_attribute == 'Type'):
            option = input('Enter (A|B|AB|O) to specify blood type: ')
            if re.match(r'^(A|B|AB|O)$', option):
                value = type_to_int(option)
                filtered = system.filter_by_attribute(attribute,value)
                return filtered
            else:
                print('Unrecognised blood type, please try again.')
                get_filter_input()
        elif (filter_attribute == 'Amount'):
            option = input('Enter amount to filter deposits by: ')
            if re.match(r'^[0-9]+$', option):
                value = int(option)
                filtered = system.filter_by_attribute(attribute,value)
                return filtered
            else:
                print('Unrecognised amount, please enter a number and try again.')
                get_filter_input()
    else:
        print('Unrecognised blood type, please try again.')
        get_filter_input()

def handle_filter():
    filtered = get_filter_input()
    display_results(filtered)

def handle_request():
    print("Please enter blood type")
    option = input('Enter (A|B|AB|O)(+-) to specify blood type: ')
    if re.match(r'^(A|B|AB|O)[+|-]$', option):
        print("blood type exists")
        amount = input('Enter amount to request: ')
        if re.match(r'^[0-9]+$', amount):
            print("ok")
        else:
            print("no")
    else:
        print("Invalid blood type. Please try again")
        handle_request()
    
logo = """
  _____         __             _____        _    
 |  __ \       / _|           |  __ \      | |   
 | |  | | __ _| |_ _ __  _   _| |  | |_   _| | __
 | |  | |/ _` |  _| '_ \| | | | |  | | | | | |/ /
 | |__| | (_| | | | | | | |_| | |__| | |_| |   < 
 |_____/ \__,_|_| |_| |_|\__, |_____/ \__,_|_|\_\\
                          __/ |                  
                         |___/                   
"""

print('\033[93m'+logo+'\033[0m')
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

user.print_instructions()

while True:

    action = input('Enter a command: ')

    if action == 'help':
        print_instructions()
    
    elif action == 'count' and type(user) is Administrator:
        handle_count()
    
    elif action == 'volume' and type(user) is Administrator:
        handle_volume()

    elif action == 'add' and type(user) is Administrator:
        handle_add()

    elif action == 'remove' and type(user) is Administrator:
        handle_remove()
    
    elif action == 'filter' and type(user) is Administrator:
        handle_filter()
    
    elif action == 'request' and type(user) is Hospital:
        handle_request()
    else:
        print('Command not recognised, please try again')
        continue
