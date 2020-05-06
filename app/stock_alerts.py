import os
import csv
import pandas as pd
import sys
import re
import datetime
import requests
import json
from dotenv import load_dotenv
from datetime import date
#from pprint import pprint

from stockage import to_usd, get_response, parsed_answer, stockage
from send_emails import send_email

load_dotenv()

MY_NAME = os.getenv("MY_NAME", default="Luke Sanders")

if __name__ == "__main__":

    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
    api_key = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")

    stocks = stockage(csv_file_path)
    print(stocks)

    action_list = stocks['daily action'].tolist()
    bad_stocks = []
    for s in action_list:
        if s < -0.005:
            bad_stocks.append(s)
    print(bad_stocks)
    stock_number = len(action_list)
    under_performers = len(bad_stocks)
    
    csv_file_path_2 = os.path.join(os.path.dirname(__file__), "..", "data", "stock_info.csv")
    stocks.to_csv(csv_file_path_2, index=False)

    writer = pd.ExcelWriter('stock_info.xlsx')
    stocks.to_excel(writer)
    writer.save()
     # invoke with default params

    #print(weather_results)

    html = ""
    html += f"<h3>Good Morning, {MY_NAME}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"
    
    html += f"<h4>Here is your update of your {stock_number} stocks <h4>"
    html += f"<p>You currently have {under_performers} under performers in your portfolio.</p>"
    html += "<p>View the Excel spreadsheet for more information</p>"

    send_email(subject="Daily Stock Alerts", html=html)