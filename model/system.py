from model.deposit import Deposit
from model.donor import Donor
from model.request import Request
from misc.read_data import get_deposits, get_donors, get_hospitals, get_requests
from misc.write_data import write_deposit, delete_deposit, write_request, write_donor, delete_donor
from misc.utility_functions import is_expired
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

    def add_donor(self, user, first_name, last_name, age, blood_type, email, allergens):
        donor_id = len(self.donors) + 1
        donor = [int(donor_id), first_name, last_name, int(age), int(blood_type), email, allergens]
        self.donors.append(donor)
        write_donor(donor, 'data/donors.csv')
    
    def remove_donor(self, donor_id):
        del self.donors[donor_id]
        delete_donor(donor_id, 'data/donors.csv')

    def add_deposit(self, donor_id, blood_type, expiry_date, amount):
        deposit_id = len(self.deposits)
        deposit = [deposit_id, donor_id, blood_type, expiry_date, amount]
        self.deposits.append(deposit)
        write_deposit(deposit, 'data/deposits.csv')

    def remove_deposit(self, deposit_id):
        del self.deposits[deposit_id]
        delete_deposit(deposit_id, 'data/deposits.csv')

    def request_blood(self, hospital_id, blood_type, amount):
        satisfiable_deposit_id = self.get_satisfiable_deposit(blood_type, amount)
        if satisfiable_deposit_id >= 0:
            request = [hospital_id, blood_type, amount, 1]
            self.remove_deposit(satisfiable_deposit_id)
            self.requests.append(request)
            write_request(request, 'data/requests.csv')
            return True
        else:
            request = [hospital_id, blood_type, amount, 0]
            self.requests.append(request)
            write_request(request, 'data/requests.csv')
            return False  
    
    def get_satisfiable_deposit(self, blood_type, amount):
        for deposit in self.deposits:
            if deposit[2] == blood_type and deposit[4] == amount and not is_expired(deposit[3]):
                return deposit[0]
        return -1


