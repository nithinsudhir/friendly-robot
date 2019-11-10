from model.deposit import Deposit
from model.donor import Donor
from model.request import Request
from misc.read_data import get_deposits, get_donors, get_hospitals, get_requests
import os


CURRENT_DIRECTORY = os.getcwd()

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

    def filter_by_attribute(self, attribute, value):
        deposits = self.deposits
        filtered = []
        i = 0
        while (i < len(deposits)):
            if (deposits[i][attribute] == value):
                filtered.append(deposits[i])
            i = i + 1

        return filtered

    #Adding a new donor record to the csv file
    def add_donor(self, user,first_name, last_name, age, blood_type, email, allergens):
        donor_list = get_donors(CURRENT_DIRECTORY + '/data/donors.csv')
        last_index = donor_list[-1][0]
        donor_id = last_index + 1
        text = ""
        try:
            with open(CURRENT_DIRECTORY + '/data/donors.csv', 'a') as donors_csv:
                text += str(donor_id) + ',' + str(first_name) + ',' + str(last_name) + ',' + str(age) + ',' + str(blood_type) + ',' + str(email) + ',' + str(allergens) + '\n'
                donors_csv.write(text)
        except IOError:
            print("File error")
            return

      

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
