import streamlit as st
import pandas as pd
import mysql.connector

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

    # Load data from the database
    query = '''
        SELECT date, open, high, low, close, volume
        FROM StockData
        WHERE symbol = 'IBM'
        ORDER BY date DESC
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    stock_df = pd.DataFrame(rows, columns=columns)

    # Streamlit Dashboard
    st.title('Financial Data Dashboard')

    # Calculate KPIs
    avg_close = stock_df['close'].mean()
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()
    total_volume = stock_df['volume'].sum()

    # Display KPIs
    st.header('Stock KPIs for IBM')
    st.metric(label="Average Closing Price", value=f"${avg_close:.2f}")
    st.metric(label="Highest Closing Price", value=f"${max_close:.2f}")
    st.metric(label="Lowest Closing Price", value=f"${min_close:.2f}")
    st.metric(label="Total Volume", value=f"{total_volume}")

    # Display data
    st.header('Stock Data')
    st.dataframe(stock_df)

except mysql.connector.Error as e:
    st.error(f"Error: {e}")

finally:
    # Close the connection
    if conn.is_connected():
        cursor.close()
        conn.close()
