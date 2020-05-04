#taken from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

import os
import csv
import sys
import re

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

if __name__ == "__main__":
 
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
    csv_headers = ['ticker', 'timestamp', 'open', 'high', 'low', 'close', 'volume']
    
    action= input('please indicate desired action (add/delete): ')
    if action == 'add':
        ticker= input('please indicate the stock ticker (lower case): ')
        if not re.match("^[a-z]*$", ticker):
            print("Error! Only letters a-z allowed!")
            sys.exit()
        elif len(ticker) > 5:
            print("Error! Only 5 characters allowed!")
            sys.exit()
        #print(ticker)
        row_dict = {'ticker': ticker,'timestamp': '','open':'','high':'','low':'', 'close':'', 'volume':''}
        append_dict_as_row(csv_file_path, row_dict, csv_headers)
    
    elif action == 'delete':
        ticker= input('please indicate the stock ticker (lower case): ')
        print(ticker)



    row_dict = {'ticker': ticker,'timestamp': '','open':'','high':'','low':'', 'close':'', 'volume':''}
 
    # Append a dict as a row in csv file
    append_dict_as_row(csv_file_path, row_dict, csv_headers)