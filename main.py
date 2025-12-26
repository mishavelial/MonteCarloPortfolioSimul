import yfinance as yf
import pandas as pd

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

print(df.head())