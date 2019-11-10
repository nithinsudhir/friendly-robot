import csv
import os
 
def write_deposit(deposit, deposits_path):
    deposit_row = ''.join(str(i) + ', ' for i in deposit).strip(', ')
    with open(deposits_path, 'a') as deposits_csv:
        deposits_csv.write(deposit_row)

def delete_deposit(deposit_id, deposits_path):
    with open(deposits_path, 'r') as csv_in:
        reader = csv.reader(csv_in)
        rows = [row for row in reader if row[0] != str(deposit_id)]
    with open(deposits_path, 'w') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerows(rows)