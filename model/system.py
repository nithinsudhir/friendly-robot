from model.deposit import Deposit
from model.donor import Donor
from model.request import Request
from read_data import get_deposits, get_donors, get_hospitals, get_requests

class System:
    def __init__(self):
        self.deposits = get_deposits('data/deposits.csv')
        self.donors = get_donors('data/donors.csv')
        self.hospitals = get_hospitals('data/hospitals.csv')
        self.requests = get_requests('data/requests.csv')

    # proposed change to get_occurrences using new data representation
    def count_deposits(self, blood_type = None):
        num_deposits = 0
        if blood_type is None:
            num_deposits = len(self.deposits)
        else:
            for deposit in self.deposits:
                current_type = deposit[2]
                if current_type == blood_type:
                    num_deposits += 1
        return num_deposits

    # proposed change to get_amount_type using new data representation
    def count_volume(self, blood_type = None):
        volume = 0
        if blood_type is None:
            for deposit in self.deposits:
                current_volume = deposit[4]
                volume += current_volume
        else:
            for deposit in self.deposits:
                current_type = deposit[2]
                current_volume = deposit[4]
                if current_type == blood_type:
                    volume += current_volume
        return volume

    # def get_occurences(self, blood_type):
    #     count = 0
    #     for item in self.blood_bank:
    #         if  item.get_blood_type() == blood_type:
    #             count += 1
    #     return count
    
    # def get_amount_type(self, blood_type):
    #     amount = 0
    #     for item in self.blood_bank:
    #         if  item.get_blood_type() == blood_type:
    #             amount+=item.get_amount()
    #     return amount

    # propose to move functionality to run.py
    # def count(self):
    #     option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
    #     if option == "":
    #         print(len(self.blood_bank))
    #     elif re.match(r"^(A|B|AB|O)[+-]$", option):
    #         count = self.get_occurences(option)
    #         print(count)
    #     else:
    #         stub()

    # propose to move functionality to run.py
    # def amount(self):
    #     option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
    #     if option == "":
    #         amount = {}
    #         for item in self.blood_bank:
    #             key = item.get_blood_type()
    #             if key in amount:
    #                 amount[key]+=item.get_amount()
    #             else:
    #                 amount[key]=item.get_amount()

    #             # amount+=item.get_amount()
    #         for key,val in amount.items():
    #             print(key, ":", round(val, 3))
    #         # print("WARNING: Total valid blood irrespective of type displayed")
    #     elif re.match(r"^(A|B|AB|O)[+-]$",option):
    #         count = self.get_amount_type(option)
    #         print(count)
    #     else:
    #         print("The type you have entered is invalid. Please try again")
    #         self.amount()

    # def add_blood_deposit(self, user, blood_type, is_valid, expiry_date, amount):
    #     # should first check if deposit is valid
    #     if user.get_user_type() == 'Administrator':
    #         with open("data/deposits.json", "r+") as deposits_file:
    #             deposits = json.load(deposits_file)
    #             new_deposit = {"Type": blood_type, "IsValid": is_valid, "expiryDate": expiry_date, "amount": amount}
    #             deposits.append(new_deposit)
    #             deposits_file.seek(0)
    #             json.dump(deposits, deposits_file, indent = 2)
    #             self.blood_bank.append(Deposit(blood_type, is_valid, expiry_date, amount))
    #             print('Sucessfully added blood deposit to system.')
    #     else:
    #         print('Could not add blood deposit - only administrators can add blood deposits.')
        
    # def remove_blood_deposit(self, user, blood_type, is_valid, expiry_date, amount):
    #     if user.get_user_type() == 'Administrator':
    #         with open("data/deposits.json", "r") as deposits_file:
    #             deposits = json.load(deposits_file)
    #         if is_valid == "true":
    #             is_valid = True
    #         else:
    #             is_valid = False
    #         amount = float(amount)
    #         new_deposit = {"Type": blood_type, "IsValid": is_valid, "expiryDate": expiry_date, "amount": amount}
    #         if new_deposit in deposits:
    #             deposits.remove(new_deposit)
    #             self.blood_bank.remove(Deposit(blood_type, is_valid, expiry_date, amount))
    #             with open("data/deposits.json", "w") as deposits_file:
    #                 json.dump(deposits, deposits_file, indent = 2)
    #                 print('Sucessfully removed blood deposit from system.')
    #     else:
    #         print('Could not remove blood deposit - only administrators can remove blood deposits.')
