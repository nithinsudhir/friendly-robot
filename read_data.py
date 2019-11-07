import csv
import os
 
def get_deposits(deposits_path):
    deposits = []
    with open(deposits_path) as deposits_csv:
        reader = csv.reader(deposits_csv, delimiter = ',')
        next(reader)    # skip first line of csv file (headings)
        for row in reader:
            deposit = [int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])]
            deposits.append(deposit)
    return deposits    

# print for debugging
print('Deposits:')
deposits = get_deposits('data/deposits.csv')
for deposit in deposits:
    print(deposit)
 
def get_donors(donors_path):
    donors = []
    with open(donors_path) as donors_csv:
        reader = csv.reader(donors_csv, delimiter = ',')
        next(reader)    # skip first line of csv file (headings)
        for row in reader:
            donor = [int(row[0]), row[1], row[2], int(row[3]), int(row[4]), row[5], row[6]]
            donors.append(donor)
    return donors
 

# print for debugging
print('\n\n')
print('Donors:')
donors = get_donors('data/donors.csv')
for donor in donors:
    print(donor)

# coming soon...
def get_hospitals(hospitals_path):
    pass