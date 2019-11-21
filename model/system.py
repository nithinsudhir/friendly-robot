from model.donor import Donor
from model.request import Request
from misc.read_data import get_deposits, get_donors, get_hospitals, get_requests
from misc.write_data import write_deposit, delete_deposit, write_request, write_donor, delete_donor
from misc.utility_functions import *
import os
import time
import datetime

CURRENT_DIRECTORY = os.getcwd()

class System:
    def __init__(self):
        self.deposits = get_deposits('data/deposits.csv')
        self.donors = get_donors('data/donors.csv')
        self.hospitals = get_hospitals('data/hospitals.csv')
        self.requests = get_requests('data/requests.csv')

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

    def get_all_blood_totals(self):
        blood_types = [0,1,2,3,4,5,6,7]
        # First create array of tuples [blood_type, volume]
        volumes = []
        for blood_type in blood_types:
            volume = self.count_volume(blood_type)
            volumes.append([blood_type,volume])
        return volumes

    def get_scarce_blood_types(self, limit):
        volumes = self.get_all_blood_totals()
        scarce = []
        i = 0
        while (i < len(volumes)):
            if (volumes[i][1] <= limit):
                scarce.append(volumes[i])
            i = i + 1

        return scarce

    def add_donor(self, first_name, last_name, age, blood_type, email, allergens):
        for donor in self.donors:
            if email.strip() == donor[5].strip():
                print("Already registered!")
                return
        donor_id = max(self.donors)[0] + 1
        donor = [int(donor_id), first_name, last_name, int(age), int(blood_type), email, allergens]
        self.donors.append(donor)
        write_donor(donor, 'data/donors.csv')
    
    def remove_donor(self, donor_id):
        self.donors.remove(self.get_donor(donor_id))
        delete_donor(donor_id, 'data/donors.csv')

    def add_deposit(self, donor_id, blood_type, expiry_date, amount):
        deposit_id = max(self.deposits)[0] + 1
        deposit = [deposit_id, donor_id, blood_type, expiry_date, amount]
        self.deposits.append(deposit)
        write_deposit(deposit, 'data/deposits.csv')

    def remove_deposit(self, deposit_id):
        self.deposits.remove(self.get_deposit(deposit_id))
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

    def get_deposit(self, deposit_id):
        for deposit in self.deposits:
            if deposit[0] == deposit_id:
                return deposit

    def get_donor(self, donor_id):
        for donor in self.donors:
            if donor[0] == donor_id:
                return donor

    def sort_by_expiry(self):
        
        print('\nDeposit ID\tDonor ID\tBlood Type\tExpiry Date\tAmount')
        print('----------------------------------------------------------------------')
    
        # Sorts with soonest expiry first
        self.deposits = sort.sort_deposits_by(3,self.deposits)

        for i in range(len(self.deposits)):
            expiry = self.deposits[i][3]
            date = datetime.datetime.fromtimestamp(expiry).strftime('%d/%m/%Y')
            date = coloured_date(expiry, date)
            b_type = self.deposits[i][2]
            out = str(int_to_blood_type(int(b_type)))
            
            print(self.deposits[i][0],'\t\t',self.deposits[i][1],'\t\t',out,'\t\t',date,'\t',self.deposits[i][4],'\t\t')
        print('\n')