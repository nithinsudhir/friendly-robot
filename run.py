from model.system import System
from model.user import User
from model.administrator import Administrator
from model.hospital import Hospital
from model.donor import Donor

def login(current_user):
    if current_user == 'A':
        return Administrator(system)
    elif current_user == 'H':
        return Hospital()
    elif current_user == 'D':
        return Donor()
    else:
        print("Invalid user. Please try again")
        current_user = input("\nPlease enter your user type (A/H/D): ")
        user = login(current_user)
        return user

system = System()

print("Welcome to the DafnyDuk Blood Managment System")

print("\nThis system accepts three different types of users:\nA - Administrator\nH - Hospital\nD - Donor")

current_user = input("\nPlease enter your user type (A/H/D): ")
user = login(current_user)

print("Logged in as "+ str(user.get_user_type()))

while True:
    action = input("Enter a command:\n")
    if action == "h":
        print("\"count\",\tview count of valid blood in bank")
        print("\"amount\",\tview amount of valid blood in bank [optionally by type]")
    elif action == "count":
        system.count()
    elif action == "amount":
        system.amount()
    elif action == "add":
        blood_type = input("Enter blood type: ")
        is_valid = input("Enter valid: ")
        expiry_date = input("Enter expiry date: ")
        amount = input("Enter amount: ")
        user.add_blood_deposit(blood_type, is_valid, expiry_date, amount)
    elif action == "remove":
        # this is an unnecessarily annoying way to remove blood deposits
        # we should add an id attribute to each blood deposit, and then remove based on id
        # donors should also have an id, and each blood deposit should have a reference to their donor id
        blood_type = input("Enter blood type: ")
        is_valid = input("Enter valid: ")
        expiry_date = input("Enter expiry date: ")
        amount = input("Enter amount: ")
        user.remove_blood_deposit(blood_type, is_valid, expiry_date, amount)
    elif action == "addDonor":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        blood_type = input("Enter blood type: ")
        allergens = input("Enter allergens: ")
        user.add_donor(first_name,last_name, age, email, phone, blood_type, allergens)
    else:
        print("Command not recognised, please try again")
        print("To view help, enter \"h\"")
