import yfinance as yf
import pandas as pd
import numpy as np

#when used for the first time, uncomment the code below
"""tickers = ['AAPL', 'MSFT', 'SPY']

df = yf.download(tickers, start='2020-01-01', end='2025-12-23')

df.to_csv('data.csv')
df = pd.read_csv('data.csv')

#deleting irrelevant columns, just for now
items = ['High', 'High.1', 'High.2' ,'Low', 'Low.1', 'Low.2', 'Open', 'Open.1', 'Open.2', 'Volume', 'Volume.1', 'Volume.2']
df.drop(columns=items, inplace=True)
df.drop(index=1, inplace=True)
df.reset_index(drop=True, inplace=True)
df.to_csv('data.csv')

df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)
df.set_index('Ticker', inplace=True)
df.to_csv('data.csv')"""

df = pd.read_csv('data.csv')

#lets start by creating some metrics which we will use for the MC method, mean, covariance and returns. first, lets log the returns so we can use them in the method, this makes it easier
df['Apple DR'] = np.log(df['AAPL']).diff().dropna()
df['Microsoft DR'] = np.log(df['MSFT']).diff().dropna()
df['S&P500 DR'] = np.log(df['SPY']).diff().dropna()

#mean and covariance
assets = ['Apple DR', 'Microsoft DR', 'S&P500 DR']

mu  = df[assets].mean()
cov = df[assets].cov()

print(mu)
print(cov)