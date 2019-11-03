import Batmobile
from Blood import Blood
import Donor
import Request
import json, re

class System:
    def __init__(self):
       self.blood_bank = init_blood_bank()

    def get_occurences(self, blood_type):
        count = 0
        for item in self.blood_bank:
            if  item.get_type() == blood_type:
                count+=1
        return count

    def get_amount_type(self, blood_type):
        amount = 0
        for item in self.blood_bank:
            if  item.get_type() == blood_type:
                amount+=item.get_amount()
        return amount

    def count(self):
        option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
        if option == "":
            print(len(self.blood_bank))
        elif re.match(r"^(A|B|AB|O)[+-]$",option):
            count = self.get_amount_type(option)
            print(count)
        else:
            stub()

    def amount(self):
        option = input("Enter (A|B|AB|O)+- to specify type [optional]:\n")
        if option == "":
            amount = 0
            for item in self.blood_bank:
                amount+=item.get_amount()
            print(amount)
            print("WARNING: Total valid blood irrespective of type displayed")
        elif re.match(r"^(A|B|AB|O)[+-]$",option):
            count = self.get_amount_type(option)
            print(count)
        else:
            stub()

def stub():
    print("This functionality is not completed yet")

def init_blood_bank():
    print("---Importing Blood---")
    bank = []

    with open("data/deposits.json") as json_file:
        blood_json = (json.load(json_file))
        for sample in blood_json:
            blood = Blood(sample["Type"],sample["IsValid"], sample["expiryDate"],sample["amount"])
            # blood.print_details()
            bank.append(blood)
    return bank



def main():
    bank = System();
    # print(bank.blood_bank)
    print("Welcome to the DafnyDuk Blood Managment System")
    print("You are logged in as administrator")
    while True:
        action = input("Enter a command:\n")
        if action == "h":
            print("\"count\",\tview count of valid blood in bank")
            print("\"amount\",\tview amount of valid blood in bank")
        elif action == "count":
            bank.count()
        elif action == "amount":
            bank.amount()
        else:
            print("Command not recognised, please try again")
            print("To view help, enter \"h\"")


if __name__ == "__main__":
    main()
