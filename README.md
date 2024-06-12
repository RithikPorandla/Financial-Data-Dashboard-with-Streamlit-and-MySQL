# Financial-Data-Dashboard-with-Streamlit-and-MySQL

This project demonstrates how to create a financial data dashboard using Python, Streamlit, and MySQL. The dashboard fetches weekly stock data from the Alpha Vantage API, stores it in a MySQL database, and visualizes key performance indicators (KPIs) and historical data in an interactive Streamlit app.

Components
1. Data Fetching Script
The fetch_alpha_vantage_data.py script is responsible for fetching weekly stock data from the Alpha Vantage API and storing it in a MySQL database. The script includes functions to:

Fetch data from the API.
Connect to the MySQL database.
Create the necessary table in the database.
Insert the fetched data into the database.

2. Streamlit Dashboard
The dashboard.py script creates an interactive dashboard using Streamlit. The dashboard:

Connects to the MySQL database.
Fetches the stored stock data.
Calculates and displays KPIs such as average closing price, highest closing price, lowest closing price, and total volume.
Displays a table of the historical stock data.
