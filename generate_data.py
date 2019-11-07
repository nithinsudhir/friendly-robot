import random
import os

NUM_DEPOSITS = 10
NUM_DONORS = 10
NUM_HOSPITALS = 10
NUM_BLOOD_TYPES = 4
BLOOD_TYPES = [i for i in range(NUM_BLOOD_TYPES)]
MIN_DATE = 0    # 01/01/2019
MAX_DATE = 1825 # 01/01/2024
MIN_DEPOSIT_AMOUNT = 50
MAX_DEPOSIT_AMOUNT = 100
MIN_AGE = 10
MAX_AGE = 100
FIRST_NAMES = ('Jack', 'Jill', 'Susan', 'Bob', 'Sam')
LAST_NAMES = ('Jones', 'Smith', 'Johnson', 'Williams', 'Wilson')
ALLERGENS = ('Peanuts', 'Penicillin', 'Cheese')

DEPOSIT_IDS = [i for i in range(NUM_DEPOSITS)]
DONOR_IDS = [i for i in range(NUM_DONORS)]
HOSPITAL_IDS = [i for i in range(NUM_HOSPITALS)]

CURRENT_DIRECTORY = os.getcwd()

# generate deposit data and write to csv file
deposits_csv = open(CURRENT_DIRECTORY + '/data/deposits.csv', 'w')
text = 'Deposit ID,Donor ID,Blood Type,Expiry Date,Amount\n'
for i in range(NUM_DEPOSITS):
    deposit_id = DEPOSIT_IDS[i]
    donor_id = DONOR_IDS[i]
    blood_type = BLOOD_TYPES[donor_id % NUM_BLOOD_TYPES]
    expiry_date = random.randint(MIN_DATE, MAX_DATE)
    amount = random.randint(MIN_DEPOSIT_AMOUNT, MAX_DEPOSIT_AMOUNT)
    text += str(deposit_id) + ',' + str(donor_id) + ',' + str(blood_type) + ',' + str(expiry_date) + ',' + str(expiry_date) + ',' + str(amount) + '\n'
 
deposits_csv.write(text)
deposits_csv.close()
 
# generate donor data and write to csv file
donors_csv = open(CURRENT_DIRECTORY + '/data/donors.csv', 'w')
text = 'Donor ID,First Name,Last Name, Age, Blood Type, Email Address, Allergens\n'
for i in range(NUM_DONORS):
    donor_id = DONOR_IDS[i]
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    age = random.randint(MIN_AGE, MAX_AGE)
    blood_type = BLOOD_TYPES[donor_id % NUM_BLOOD_TYPES]
    email_address = first_name + last_name + '@gmail.com'
    allergens = random.choice(ALLERGENS)
    text += str(donor_id) + ',' + str(first_name) + ',' + str(last_name) + ',' + str(age) + ',' + str(blood_type) + ',' + str(email_address) + ',' + str(allergens) + '\n'
 
donors_csv.write(text)
donors_csv.close()

# generate hospital data and write to csv file
hospitals_csv = open(CURRENT_DIRECTORY + '/data/hospitals.csv', 'w')
text = 'Hospital ID, X-Coordinate, Y-Coordinate\n'
for i in range(NUM_DONORS):
    hospital_id = HOSPITAL_IDS[i]
    x_coordinate = random.randint(0, NUM_HOSPITALS)
    y_coordinate = random.randint(0, NUM_HOSPITALS)
    text += str(hospital_id) + ',' + str(x_coordinate) + ',' + str(y_coordinate) + '\n'

hospitals_csv.write(text)
hospitals_csv.close()