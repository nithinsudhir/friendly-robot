from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor

print("Welcome to the DafnyDuk Blood Managment System")

print("\nThis system accepts three different types of users:\nA - Administrator\nH - Hospital\nD - Donor")

current_user = input("\nPlease enter your user type (A/H/D): ")

if current_user == 'A':
    current_user = Administrator()
elif current_user == 'H':
    current_user = Hospital()
elif current_user == 'D':
    current_user = Donor()
else:
    exit()

print(f'You are logged in as a {current_user.get_user_type()}\n')

system = System()

while True:
    action = input("Enter a command:\n")
    if action == "h":
        print("\"count\",\tview count of valid blood in bank")
    elif action == "count":
        system.count()
    else:
        print("Command not recognised, please try again")
        print("To view help, enter \"h\"")