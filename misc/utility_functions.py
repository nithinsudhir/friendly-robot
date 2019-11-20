# Useful functions that do not belong to any particular module
import misc.sort as sort

import time
import datetime

def type_to_int(blood_type):
    if blood_type == 'A+':
        return 0
    elif blood_type == 'A-':
        return 1
    elif blood_type == 'B+':
        return 2
    elif blood_type == 'B-':
        return 3
    elif blood_type == 'AB+':
        return 4
    elif blood_type == 'AB-':
        return 5
    elif blood_type == 'O+':
        return 6
    elif blood_type == 'O-':
        return 7

def int_to_blood_type(blood_type):
    if blood_type == 0:
        return 'A+'
    elif blood_type == 1:
        return 'A-'
    elif blood_type == 2:
        return 'B+'
    elif blood_type == 3:
        return 'B-'
    elif blood_type == 4:
        return 'AB+'
    elif blood_type == 5:
        return 'AB-'
    elif blood_type == 6:
        return 'O+'
    elif blood_type == 7:
        return 'O-'

def attribute_to_int(attribute):
    if attribute == 'Type':
        return 2
    elif attribute == 'Amount':
        return 4

def date_to_int(date):
    return int(time.mktime(datetime.datetime.strptime(date, '%d/%m/%Y').timetuple()))

def is_expired(expriy_date_int):
    current_date = datetime.datetime.today().strftime('%d/%m/%Y')
    current_date_int = date_to_int(current_date)
    if current_date_int > expriy_date_int:
        return True
    else:
        return False
    
def coloured_date(expiry,date):
    if is_expired(expiry):
        return '\033[93m'+date+'\033[0m'
    else:
        return '\033[92m'+date+'\033[0m'

def display_results(deposits):
    print('\nDeposit ID\tDonor ID\tBlood Type\tExpiry Date\tAmount')
    print('----------------------------------------------------------------------')
    
    # Sorts with soonest expiry first
    deposits = sort.sort_deposits_by(3,deposits)

    for i in range(len(deposits)):
        expiry = deposits[i][3]
        date = datetime.datetime.fromtimestamp(expiry).strftime('%d/%m/%Y')
        date = coloured_date(expiry, date)
        print(deposits[i][0],'\t\t',deposits[i][1],'\t\t',deposits[i][2],'\t\t',date,'\t\t',deposits[i][4],'\t\t')
    print('\n')

def print_scarce_blood(volumes):
    if (volumes != []):
        print("\nWARNING: Scarce blood types listed below:\n")
        print('Blood Type\tAmount')
        print('---------------------------------')
        for i in range(len(volumes)):
            print(int_to_blood_type(volumes[i][0]),'\t\t',volumes[i][1])
        print('\n')
