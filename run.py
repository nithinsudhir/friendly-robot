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
    print('add deposit - add blood deposit to system')
    print('remove deposit - remove blood deposit from system')
    print('help - print all available commands')

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

def handle_add_deposit():
    donor_id = int(input('Enter donor ID: '))
    blood_type = type_to_int(input('Enter blood type (A|B|AB|O): '))
    expiry_date = date_to_int(input('Enter expiry date (dd/mm/yyyy): '))
    amount = int(input('Enter amount: '))
    user.add_deposit(donor_id, blood_type, expiry_date, amount)
    print('Deposit added successfully')

def handle_remove_deposit():
    deposit_id = int(input('Enter deposit ID: '))
    user.remove_deposit(deposit_id)
    print('Deposit removed successfully')

def handle_filter():
    filter_attribute = input('Enter (Type | Amount) to specify filter attribute: ')
    if re.match(r'^(Type|Amount)$', filter_attribute):
        attribute = attribute_to_int(filter_attribute)
        if (filter_attribute == 'Type'):
            option = input('Enter (A|B|AB|O) to specify blood type: ')
            if re.match(r'^(A|B|AB|O)$', option):
                value = type_to_int(option)
                filtered = system.filter_by_attribute(attribute,value)
                display_results(filtered)
            else:
                print('Unrecognised blood type, please try again.')
                handle_filter()
        elif (filter_attribute == 'Amount'):
            option = input('Enter amount to filter deposits by: ')
            if re.match(r'^[0-9]+$', option):
                value = int(option)
                filtered = system.filter_by_attribute(attribute,value)
                display_results(filtered)
            else:
                print('Unrecognised amount, please enter a number and try again.')
                handle_filter()
    else:
        print('Unrecognised blood type, please try again.')
        handle_filter()
    
    

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

    elif action == 'add deposit':
        handle_add_deposit()

    elif action == 'remove deposit':
        handle_remove_deposit()
    
    elif action == 'filter':
        handle_filter()

    elif action == 'addDonor':
        if(user.get_user_type() != 'Administrator'):
            print ("Only Administrators can add donors")
            continue
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = input("Enter age: ")
        blood_type = input("Enter blood type: ")
        email = input("Enter email: ")
        allergens = input("Enter allergens: ")
        user.add_donor(first_name, last_name, age, blood_type, email, allergens)

    else:
        print('Command not recognised, please try again')
        continue
