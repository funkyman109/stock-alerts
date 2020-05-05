#taken from https://docs.python.org/3.4/library/csv.html?highlight=csv

import csv
import os

def write_csv(csv_file_path, csv_headers):
    with open(csv_file_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
csv_headers = ['ticker', 'timestamp', 'open', 'high', 'low', 'close', 'volume', 'daily action']

#taken from https://stackoverflow.com/questions/12277864/python-clear-csv-file
f = open(csv_file_path, "w")
f.truncate()
f.close()
write_csv(csv_file_path, csv_headers)