import mysql.connector
import requests
import json
from datetime import datetime
from mysql.connector import Error

# API key for Alpha Vantage
api_key = 'ZPPJ5WYNU0C8FEK8'
symbol = 'IBM'  # Example stock symbol

# Function to fetch stock data
def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Print the response for debugging
        return data
    else:
        print(f"Error fetching data for {symbol}: {response.status_code}, {response.text}")
        return None

# Function to connect to MySQL database
def connect_to_mysql():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='1234',
        database='stock'
    )

try:
    # Connect to MySQL database
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StockData (
            symbol VARCHAR(10),
            date DATE,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT,
            PRIMARY KEY (symbol, date)
        )
    ''')

    # Fetch and insert stock data
    data = fetch_stock_data(symbol)
    if data and 'Weekly Time Series' in data:
        time_series = data['Weekly Time Series']
        for date, values in time_series.items():
            try:
                print(f"Date: {date}, Values: {values}")  # Print data to verify
                cursor.execute('''
                    INSERT IGNORE INTO StockData (symbol, date, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (
                    symbol,
                    date,
                    float(values['1. open']),
                    float(values['2. high']),
                    float(values['3. low']),
                    float(values['4. close']),
                    int(values['5. volume'])
                ))
            except Exception as e:
                print(f"Error inserting data for {date}: {e}")
    else:
        print("No data found for the symbol or incorrect API key.")

    # Commit and close connection
    conn.commit()
    cursor.close()
    conn.close()

except Error as e:
    print(f"Error: {e}")
