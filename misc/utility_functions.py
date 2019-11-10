# Useful functions that do not belong to any particular module
import misc.sort as sort

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

def display_results(deposits):
    print('\nDeposit ID\tDonor ID\tBlood Type\tExpiry Date\tAmount')
    print('----------------------------------------------------------------------')
    
    # Sorts with soonest expiry first
    deposits = sort.sort_deposits_by(3,deposits)

    for i in range(len(deposits)):
        print(deposits[i][0],'\t\t',deposits[i][1],'\t\t',deposits[i][2],'\t\t',deposits[i][3],'\t\t',deposits[i][4],'\t\t')
    print('\n')
        
