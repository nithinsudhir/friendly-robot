from .deposit import Deposit
from .donor import Donor
from .request import Request
import json, re

class System:
    def __init__(self):
       self.blood_bank = init_blood_bank()

    def get_occurences(self, blood_type):
        count = 0
        for item in self.blood_bank:
            if  item.get_blood_type() == blood_type:
                count += 1
        return count

    def count(self):
        option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
        if option == "":
            print(len(self.blood_bank))
        elif re.match(r"^(A|B|AB|O)[+-]$", option):
            count = self.get_occurences(option)
            print(count)
        else:
            stub()

    def print_deposits(self):
        for blood_deposit in self.blood_bank:
            print(blood_deposit)

def stub():
    print("This functionality is not completed yet")

def init_blood_bank():
    print("---Importing Blood---")
    bank = []

    with open("data/deposits.json") as json_file:
        blood_json = (json.load(json_file))
        for sample in blood_json:
            deposit = Deposit(sample["Type"],sample["IsValid"], sample["expiryDate"],sample["amount"])
            # print(deposit)
            bank.append(deposit)
    return bank
