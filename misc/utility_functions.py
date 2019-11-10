# Useful functions that do not belong to any particular module

import time
import datetime

def type_to_int(blood_type):
    if blood_type == 'A':
        return 0
    elif blood_type == 'B':
        return 1
    elif blood_type == 'AB':
        return 2
    elif blood_type == 'O':
        return 3

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

def display_results(deposits):
    print('\nDeposit ID\tDonor ID\tBlood Type\tExpiry Date\tAmount')
    print('----------------------------------------------------------------------')
    for i in range(len(deposits)):
        print(deposits[i][0],'\t\t',deposits[i][1],'\t\t',deposits[i][2],'\t\t',deposits[i][3],'\t\t',deposits[i][4],'\t\t')
    print('\n')
