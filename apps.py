
import pandas as pd
import yfinance as yf
import numpy as np

# a hands on with dataFrames
df = pd.DataFrame([[2, 3], [3, 4], [5, 6]], index=[
                  'cobra', 'viper', 'side'], columns=['max', 'rex'])
df = df.loc[:, 'max']
print(df.index)  # to list indices
# print(df)

# to download data
# df_yahoo = yf.download('AAPL', start='2000-01-01', end = '2010-01-01', progress = False)
# msft = yf.Ticker("MSFT")


df = yf.download('AAPL',
                 start='2000-01-01',
                 end='2010-12-31',
                 progress=False)

# to find returns: Simple and logarithm

df = df.loc[:, ['Adj Close']]
df.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
df['simple_rtn'] = df.adj_close.pct_change()
df['log_rtn'] = np.log(df.adj_close/df.adj_close.shift(1))
