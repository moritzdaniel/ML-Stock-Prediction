import yfinance as yf
import pandas as pd

# Download stock data for Apple (AAPL)
ticker = 'AAPL'
stock_data = yf.download(ticker, start='2010-01-01', end='2023-01-01')

# Show the first few rows
print(stock_data.head())
