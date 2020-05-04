import csv
import json
import os
import pandas as pd
import re
import sys
import datetime
import dotenv 
import requests

dotenv.load_dotenv()




def write_csv(csv_file_path, csv_headers):
    """
    writes currently existing json data into a csv file to be used later
    """
    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices= tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": daily_prices['1. open'],
                "high": daily_prices['2. high'],
                "low": daily_prices['3. low'],
                "close": daily_prices['4. close'],
                "volume": daily_prices['5. volume'],
            })

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
csv_headers = ['timestamp', 'open', 'high', 'low', 'close', 'volume']