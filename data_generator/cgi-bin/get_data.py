#!/usr/bin/env python3
import csv
import json
from datetime import datetime
import random

# Empty dictionary

data = []
# function to read csv and convert to dict
def csv_to_dict(csv_filepath):
   with open(csv_filepath, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)

    
# File to read
csv_file = 'retail_store_inventory.csv'

# Read CSV into dict
csv_to_dict(csv_file)

# Data is 73100 lines, pick one at random
random_integer = random.randint(1, 73100) 

# Grab a random record
record_to_return = data[random_integer]

# Get current time
now = datetime.now()

# format the time
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Set date of dataset to now
record_to_return['Date'] = dt_string

data = (json.dumps(record_to_return))

#data = f'{{"name": "{i}"}}'
#data = '{"name": "tom"}'
print(
"""\
Content-Type: application/json
"""
)

print(data)
