
import pandas as pd
import yfinance as yf


df_yahoo = yf.download('AAPL', start='2000-01-01',
                       end='2010-01-01', progress=False)

msft = yf.Ticker("MSFT")
print(msft)

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits
