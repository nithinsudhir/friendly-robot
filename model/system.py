from .deposit import Deposit
from .donor import Donor
from .request import Request
import json, re

class System:
    def __init__(self):
       self.blood_bank = init_blood_bank()
       self.donors = init_donors()
       

    def get_occurences(self, blood_type):
        count = 0
        for item in self.blood_bank:
            if  item.get_blood_type() == blood_type:
                count += 1
        return count
    
    def get_amount_type(self, blood_type):
        amount = 0
        for item in self.blood_bank:
            if  item.get_blood_type() == blood_type:
                amount+=item.get_amount()
        return amount

    def count(self):
        option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
        if option == "":
            print(len(self.blood_bank))
        elif re.match(r"^(A|B|AB|O)[+-]$", option):
            count = self.get_occurences(option)
            print(count)
        else:
            stub()

    def amount(self):
        option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
        if option == "":
            amount = {}
            for item in self.blood_bank:
                key = item.get_blood_type()
                if key in amount:
                    amount[key]+=item.get_amount()
                else:
                    amount[key]=item.get_amount()

                # amount+=item.get_amount()
            for key,val in amount.items():
                print(key, ":", round(val, 3))
            # print("WARNING: Total valid blood irrespective of type displayed")
        elif re.match(r"^(A|B|AB|O)[+-]$",option):
            count = self.get_amount_type(option)
            print(count)
        else:
            print("The type you have entered is invalid. Please try again")
            self.amount()

    def print_deposits(self):
        for blood_deposit in self.blood_bank:
            print(blood_deposit)

    def add_blood_deposit(self, user, blood_type, is_valid, expiry_date, amount):
        # should first check if deposit is valid
        if user.get_user_type() == 'Administrator':
            with open("data/deposits.json", "r+") as deposits_file:
                deposits = json.load(deposits_file)
                new_deposit = {"Type": blood_type, "IsValid": is_valid, "expiryDate": expiry_date, "amount": amount}
                deposits.append(new_deposit)
                deposits_file.seek(0)
                json.dump(deposits, deposits_file, indent = 2)
                self.blood_bank.append(Deposit(blood_type, is_valid, expiry_date, amount))
                print('Sucessfully added blood deposit to system.')
        else:
            print('Could not add blood deposit - only administrators can add blood deposits.')
        
    def remove_blood_deposit(self, user, blood_type, is_valid, expiry_date, amount):
        if user.get_user_type() == 'Administrator':
            with open("data/deposits.json", "r") as deposits_file:
                deposits = json.load(deposits_file)
            if is_valid == "true":
                is_valid = True
            else:
                is_valid = False
            amount = float(amount)
            new_deposit = {"Type": blood_type, "IsValid": is_valid, "expiryDate": expiry_date, "amount": amount}
            if new_deposit in deposits:
                deposits.remove(new_deposit)
                self.blood_bank.remove(Deposit(blood_type, is_valid, expiry_date, amount))
                with open("data/deposits.json", "w") as deposits_file:
                    json.dump(deposits, deposits_file, indent = 2)
                    print('Sucessfully removed blood deposit from system.')
        else:
            print('Could not remove blood deposit - only administrators can remove blood deposits.')



       
    def add_donor(self, user, first_name, last_name, age, email, phone, blood_type, allergens):
        
        print("Inside system: add donor")
        if user.get_user_type() == 'Administrator':
            with open("data/donors.json", "r+") as donors_file:
                print ("Opened json file")
                donors = json.load(donors_file)
                new_donor = {"firstname": first_name, "lastname": last_name,"age": age, "email": email, "phone": phone,"bloodType": blood_type, "allergens": allergens}
                donors.append(new_donor)
                print("Appended to json")
                donors_file.seek(0)
                json.dump(donors, donors_file, indent = 2)
                self.donors.append(Donor(first_name, last_name, age, email, phone, blood_type, allergens))
                print('Sucessfully added donor to system.')
        else:
            print('Could not add donor record - only administrators can add new donors.')

    


def stub():
    print("This functionality is not completed yet")

def init_blood_bank():
    print("---Importing Blood---")
    bank = []

    with open("data/deposits.json") as json_file:
        blood_json = (json.load(json_file))
        for sample in blood_json:
            deposit = Deposit(sample["Type"],sample["IsValid"], sample["expiryDate"],sample["amount"])
            print(deposit)
            bank.append(deposit)
    return bank

def init_donors():
    print("---Importing Donor Records---")
    registered_donors = []

    with open("data/donors.json") as json_file:
        donors = (json.load(json_file))
        for sample in donors:
            donor = Donor(sample["firstname"], sample["lastname"], sample["age"], sample["email"], sample["phone"], sample["bloodType"], sample["allergens"])
            print (donor)
            registered_donors.append(donor)
    return registered_donors