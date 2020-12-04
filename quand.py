import pandas as pd
import quandl
from settings import Q_API
import yfinance as yf
import numpy as np
quandl.ApiConfig.api_key = Q_API


def realized_volatility(x):
    return np.sqrt(np.sum(x**2))


df = yf.download('AAPL',
                 start='2000-01-01',
                 end='2010-12-31',
                 progress=False)

# to find returns: Simple and logarithm

df = df.loc[:, ['Adj Close']]
df.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
df['simple_rtn'] = df.adj_close.pct_change()
df['log_rtn'] = np.log(df.adj_close/df.adj_close.shift(1))

# creating a dataframe of only dates as index
df_all_dates = pd.DataFrame(index=pd.date_range(start='1999-12-31',
                                                end='2010-12-31'))

# Just like pandas dropna() method manage and remove Null values from a data frame,
# fillna() manages and let the user replace NaN values with some value of their own.
# here M denotes Month end frequency

df = df_all_dates.join(df[['adj_close']], how='left').fillna(
    method='ffill').asfreq('M')
# print(df)

# Now get the CPI data and merge it with df using date column
df_cpi = quandl.get(dataset='RATEINF/CPI_USA',
                    start_date='1999-12-01',
                    end_date='2010-12-31')
df_cpi.rename(columns={'Value': 'cpi'}, inplace=True)

"""
               
Date          cpi
1999-12-31  168.300
2000-01-31  168.800
2000-02-29  169.800
2000-03-31  171.000
"""


df_merged = df.join(df_cpi, how='left')
"""
print(df_merged)

            adj_close      cpi
1999-12-31   0.785456  168.300
2000-01-31   0.792618  168.800
2000-02-29   0.875700  169.800

"""
df_merged['simple_rtn'] = df_merged.adj_close.pct_change()
df_merged['inflation_rate'] = df_merged.cpi.pct_change()
# print(df_merged.simple_rtn)
df_merged['real_rtn'] = (df_merged.simple_rtn + 1) * \
    (df_merged.inflation_rate + 1) - 1

# print(df_merged)

"""
   adj_close      cpi  simple_rtn  inflation_rate  real_rtn
1999-12-31   0.785456  168.300         NaN             NaN       NaN
2000-01-31   0.792618  168.800    0.009118        0.002971  0.012116
2000-02-29   0.875700  169.800    0.104819        0.005924  0.111364
2000-03-31   1.037565  171.200    0.184842        0.008245  0.194611

"""
