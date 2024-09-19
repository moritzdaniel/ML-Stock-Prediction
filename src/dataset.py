import yfinance as yf
import pandas as pd

# Download stock data for Apple (AAPL)
ticker = "AAPL"
stock_data = yf.download(ticker, start="2010-01-01", end="2023-01-01")

# Show the first few rows
print(stock_data.head())

import matplotlib.pyplot as plt

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(stock_data["Close"], label=f"{ticker} Closing Price")
plt.title(f"{ticker} Stock Price (2010-2023)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
