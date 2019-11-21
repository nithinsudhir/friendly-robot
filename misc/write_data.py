import csv
import os
 
def write_deposit(deposit, deposits_path):
    deposit_row = ''.join(str(i) + ', ' for i in deposit).strip(', ') + '\n'
    with open(deposits_path, 'a') as deposits_csv:
        deposits_csv.write(deposit_row)

def delete_deposit(deposit_id, deposits_path):
    with open(deposits_path, 'r') as csv_in:
        reader = csv.reader(csv_in)
        rows = [row for row in reader if row and row[0] != str(deposit_id)]
    with open(deposits_path, 'w') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerows(rows)

def write_request(request, requests_path):
    request_row = ''.join(str(i) + ', ' for i in request).strip(', ') + '\n'
    with open(requests_path, 'a') as requests_csv:
        requests_csv.write(request_row)

def write_donor(donor, donor_path):
    donor = ''.join(str(i) + ', ' for i in donor).strip(', ') + '\n'
    with open(donor_path, 'a') as donors_csv:
        donors_csv.write(donor)

def delete_donor(donor_id, donor_path): 
    with open(donor_path, 'r') as inp:
        reader = csv.reader(inp)
        rows = [row for row in reader if row and row[0] != str(donor_id)]
    with open(donor_path,'w') as out:
        writer = csv.writer(out)
        writer.writerows(rows)
