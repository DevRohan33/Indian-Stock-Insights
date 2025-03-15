# 📊 NSE Stock Analysis

**NSE Stock Analysis** is a Python-based project that **fetches real-time stock market data**, analyzes trends, and presents the results in a **beautifully formatted HTML table**. This project helps users track **top growth stocks, least moving stocks, and most declined stocks** based on NSE market data.

## 🚀 Features

✅ **Fetches real-time stock data** from [Twelve Data API](https://www.twelvedata.com/)  
✅ **Analyzes stock performance** (growth, least moving, and most declined stocks)  
✅ **Auto-generates a well-structured HTML table**  
✅ **Easy-to-read stock analysis page**  
✅ **Displays stock trends and percentage changes**  

## Demo 
![Screenshot 2025-03-15 182112](https://github.com/user-attachments/assets/cab04ad2-403e-4f5a-871c-5dbae92bbf18)


## 📂 Project Structure
```bash
📂 NSE-Stock-Analysis
│── 📂 env/                  # Stores API key securely
│   ├── .env                 # API key file
│── 📂 data/                 # Stores stock data
│   ├── stocks_data.csv      # Auto-generated stock data
│   ├── stocks_table.html    # Auto-generated stock analysis table
│── ├── fetch_stocks_twelve.py  # Fetches stock data from Twelve Data API
│── ├── generate_html.py     # Converts CSV to HTML table
│── ├── requirements.txt     # Dependencies list
│── ├── README.md            # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository and install package**
```bash
git clone https://github.com/DevRohan33/Indian-Stock-Insights.git
```
```bash
cd IndianStockData
```
```bash
pip install -r requirements.txt
```
## 2️⃣ **Set Up Your API Key**
- Sign up on Twelve Data
- Get your FREE API Key
- Open the .env file inside the env/ folder and ad
```bash
TWELVE_DATA_API_KEY=YOUR_NEW_TWELVE_DATA_API_KEY
```
## 3️⃣ **Fetch Live Stock Data**
```bash
python fetch_stocks_api.py
```
## 4️⃣ **Generate Stock Analysis Table**
```bash
python generate_html.py
```
## 5️⃣ **Open the Stock Analysis Page**
- Open data/stocks_table.html in your browser 📊
- 
## 🤝 **Contributing**
- Fork the repository
- Create a new branch (feature-new-update)
- Commit changes & submit a pull request

## ⭐ **Show Your Support**
If you found this project helpful, consider starring ⭐ the repository on GitHub!Happy Coding! 🚀🔥


