from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor

def login(current_user):
    if current_user == 'A':
        return Administrator()
    elif current_user == 'H':
        return Hospital()
    elif current_user == 'D':
        return Donor()
    else:
        print("Invalid user. Please try again")
        current_user = input("\nPlease enter your user type (A/H/D): ")
        user = login(current_user)
        return user
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
print("Welcome to the DafnyDuk Blood Managment System")

print("\nThis system accepts three different types of users:\nA - Administrator\nH - Hospital\nD - Donor")

current_user = input("\nPlease enter your user type (A/H/D): ")
user = login(current_user)

print("Logged in as "+ str(user.get_user_type()))

system = System()

while True:
    action = input("Enter a command:\n")
    if action == "h":
        print("\"count\",\tview count of valid blood in bank")
        print("\"amount\",\tview amount of valid blood in bank [optionally by type]")
    elif action == "count":
        system.count()
    elif action == "amount":
        system.amount()
    else:
        print("Command not recognised, please try again")
        print("To view help, enter \"h\"")
