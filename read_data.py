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
print('\n\n')
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


def get_hospitals(hospitals_path):
    hospitals = []
    with open(hospitals_path) as hospitals_csv:
        reader = csv.reader(hospitals_csv, delimiter = ',')
        next(reader)    # skip first line of csv file (headings)
        for row in reader:
            hospital = [int(row[0]), int(row[1]), int(row[2])]
            hospitals.append(hospital)
    return hospitals

# print for debugging
print('\n\n')
print('Hospitals:')
hospitals = get_hospitals('data/hospitals.csv')
for hospital in hospitals:
    print(hospital)

def get_requests(requests_path):
    requests = []
    with open(requests_path) as requests_csv:
        reader = csv.reader(requests_csv, delimiter = ',')
        next(reader)    # skip first line of csv file (headings)
        for row in reader:
            request = [int(row[0]), int(row[1]), int(row[2]), int(row[3])]
            requests.append(request)
    return requests

# print for debugging
print('\n\n')
print('Requests:')
requests = get_requests('data/requests.csv')
for request in requests:
    print(request)