import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv("env/.env")
API_KEY = os.getenv("TWELVE_DATA_API_KEY")

if not API_KEY:
    raise ValueError("API Key is missing! Set it in the .env file.")

# Define stock symbols (NSE format supported by Twelve Data)
stocks = ["RELIANCE:NSE", "INFY:NSE", "TCS:NSE", "HDFCBANK:NSE", "HINDUNILVR:NSE"]

BASE_URL = "https://api.twelvedata.com/time_series"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Function to fetch stock data
def fetch_stock_data(symbol):
    params = {
        "symbol": symbol,
        "interval": "1h",
        "apikey": API_KEY,
        "format": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(f" API Response for {symbol}:\n", data)  # Debugging

    if "values" not in data:
        print(f"Error fetching data for {symbol}: {data.get('message', 'Unknown error')}")
        return None

    df = pd.DataFrame(data["values"])
    df = df.rename(columns={"datetime": "Datetime"})
    df["Stock"] = symbol
    return df

# Fetch data for all stocks with a delay to avoid rate limits
all_data = []

for stock in stocks:
    print(f"Fetching data for {stock}...")
    df = fetch_stock_data(stock)
    if df is not None:
        all_data.append(df)

    time.sleep(1)  # Add 1-second delay to avoid rate limits

# Save to CSV if data is available
if all_data:
    final_df = pd.concat(all_data)
    final_df.to_csv("data/stocks_data.csv", index=False)
    print("Stock data saved in `data/stocks_data.csv`")
else:
    print("No stock data fetched.")
