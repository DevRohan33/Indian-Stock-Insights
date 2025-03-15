import pandas as pd

# Read the CSV file
csv_file = "data/stocks_data.csv"

try:
    df = pd.read_csv(csv_file)

    # Ensure proper column order for display
    df = df[['Datetime', 'Stock', 'open', 'high', 'low', 'close', 'volume']]

    # Convert columns to numeric for analysis
    df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric)

    # Calculate stock performance
    df['Price Change'] = df['close'] - df['open']
    df['% Change'] = ((df['Price Change'] / df['open']) * 100).round(2)

    # Identify stock performance categories
    top_growth = df.groupby('Stock')['% Change'].mean().nlargest(3)
    least_moving = df.groupby('Stock')['% Change'].mean().nsmallest(3, keep='all')
    most_down = df.groupby('Stock')['% Change'].mean().nsmallest(3)

    # Create an analysis table DataFrame
    analysis_df = pd.DataFrame({
        "Category": ["🏆 Top Growth Stocks", "⚖️ Least Moving Stocks", "📉 Most Declined Stocks"],
        "Stock": [top_growth.index[0], least_moving.index[0], most_down.index[0]],
        "Average % Change": [top_growth.iloc[0], least_moving.iloc[0], most_down.iloc[0]]
    })

    # Convert DataFrames to HTML tables
    analysis_table = analysis_df.to_html(index=False, classes="styled-table")
    stock_table = df.to_html(index=False, classes="styled-table")

    # Generate HTML with styling
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stock Market Analysis</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 20px;
            }}
            .container {{
                width: 90%;
                margin: 0 auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
            }}
            .styled-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 18px;
                text-align: left;
            }}
            .styled-table th, .styled-table td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
            }}
            .styled-table th {{
                background-color: #4CAF50;
                color: white;
            }}
            .highlight-up {{
                background-color: #d4edda;
                color: #155724;
            }}
            .highlight-down {{
                background-color: #f8d7da;
                color: #721c24;
            }}
            .highlight-neutral {{
                background-color: #fff3cd;
                color: #856404;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Stock Market Analysis</h1>
            
            <h2>Stock Performance Overview</h2>
            {analysis_table}

            <h2>Full Stock Data</h2>
            {stock_table}
        </div>
    </body>
    </html>
    """

    # Save the HTML file
    output_file = "data/stocks_table.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML table generated: data/stocks_table.html")

except Exception as e:
    print(f" Error: {e}")
