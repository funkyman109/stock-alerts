import csv
import pandas as pd
import os
import sys
import re
import datetime
import dotenv 
import requests
import json

dotenv.load_dotenv()

def to_usd(price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${price:,.2f}" #> $12,000.71

def get_response(symbol, api_key):
    """
    will pull stock information from api based on ticker symbol
    """
    pull = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}")
    return pull
    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=aapl&apikey=4LWE27AHC1A06OCK

def parsed_answer(response):
    """
    will format requested data in a json loaded format
    """
    output= response.text
    parsed_response = json.loads(output)
    return parsed_response

if __name__ == "__main__":
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
    Daytime = datetime.datetime.now()
    api_key = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")
    df = pd.read_csv(csv_file_path)
    #print(df)
    for row in df.index:
        symbol = df['ticker'][row]
        response = get_response(symbol, api_key)
        parsed_response = parsed_answer(response)
        #last_refresh = parsed_response["Meta Data"]["3. Last Refreshed"]
        tsd = parsed_response['Time Series (Daily)']
        dates = list(tsd.keys())
        latest_date = dates[0]
        latest_open = float(tsd[latest_date]['1. open'])
        latest_high = float(tsd[latest_date]['2. high'])
        latest_low = float(tsd[latest_date]['3. low'])
        latest_close = float(tsd[latest_date]['4. close'])
        latest_volume = float(tsd[latest_date]['5. volume'])
        daily_action = (latest_open-latest_close)/latest_open
        #df['timestamp'][row]= last_refresh
        df['open'][row] = to_usd(latest_open)
        df['high'][row] = to_usd(latest_high)
        df['low'][row] = to_usd(latest_low)
        df['close'][row] = to_usd(latest_close)
        df['volume'][row] = latest_volume
        df['daily action'][row] = daily_action
        print(symbol, latest_open, latest_high, latest_low, latest_close, latest_volume, daily_action)
    
    print(df)

    csv_file_path_2 = os.path.join(os.path.dirname(__file__), "..", "data", "stock_info.csv")
    df.to_csv(csv_file_path_2, index=False)
