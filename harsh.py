import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from arch import arch_model
import datetime as dt

years = 25
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365 * years)
tickers = ['SPY', 'BND', 'GLD', 'QQQ', 'VTI']
adj_close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=startDate, end=endDate)
    
     
    if 'Adj Close' in data.columns:
        adj_close_df[ticker] = data['Adj Close']
    else:
        print(f"Warning: 'Adj Close' not found for {ticker}")
        adj_close_df[ticker] = data['Close']  # Fallback to 'Close' if 'Adj Close' is not available

print(adj_close_df)
log_returns = np.log(adj_close_df/adj_close_df.shift(1))
log_returns = log_returns.dropna()
print(log_returns)
portfolio_value = 3500000
weights = np.array([1/len(tickers)]*len(tickers))
print(weights)
historical_returns = (log_returns*weights).sum(axis=1)
print(historical_returns)
days = 5
range_returns = historical_returns.rolling(window = days).sum()
range_returns = range_returns.dropna()
print(range_returns)
confidence_interval = 0.95
VaR = -np.percentile(range_returns, 100 - (confidence_interval * 100))*portfolio_value
print(VaR)
