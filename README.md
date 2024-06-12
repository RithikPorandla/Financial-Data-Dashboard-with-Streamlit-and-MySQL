# Financial-Data-Dashboard-with-Streamlit-and-MySQL

## Overview

This project demonstrates how to create a financial data dashboard using Python, Streamlit, and MySQL. The dashboard fetches weekly stock data from the Alpha Vantage API, stores it in a MySQL database, and visualizes key performance indicators (KPIs) and historical data in an interactive Streamlit app.

## Components

### 1. Data Fetching Script
The `finance.py` script is responsible for fetching weekly stock data from the Alpha Vantage API and storing it in a MySQL database. The script includes functions to:
- Fetch data from the API.
- Connect to the MySQL database.
- Create the necessary table in the database.
- Insert the fetched data into the database.

### 2. Streamlit Dashboard
The `dashboard_stock.py` script creates an interactive dashboard using Streamlit. The dashboard:
- Connects to the MySQL database.
- Fetches the stored stock data.
- Calculates and displays KPIs such as average closing price, highest closing price, lowest closing price, and total volume.
- Displays a table of the historical stock data.

## Example Output

### KPIs
- **Average Closing Price**: Displays the average closing price of the stock.
- **Highest Closing Price**: Shows the highest closing price of the stock.
- **Lowest Closing Price**: Shows the lowest closing price of the stock.
- **Total Volume**: Displays the total trading volume of the stock.

### Historical Data
A table displaying the historical weekly stock data including open, high, low, close prices, and volume.

## Conclusion

This project provides a simple yet powerful example of how to integrate various technologies to build a financial dashboard. By using Python, Streamlit, and MySQL, you can create an interactive and informative application that can be expanded and customized for various financial data analysis needs.
