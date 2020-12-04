import pandas as pd
index_values = (pd.date_range('1/1/2000',

                              periods=17, freq='W'))

# use M and W to see the effect of asfreq with fill_value argument

series = (pd.Series([0.0, None, 2.0, None, 5, 6, 7, 4, 5, 6, 7, None, 4, 5, 6, 7, 10],
                    index=index_values))
df = pd.DataFrame({"Col_1": series})

# to generate the data of month end only
df1 = df.asfreq(freq='M', fill_value=9.0)
# if something is already created: fill_value will not insert the value
df2 = df.asfreq(freq='D', fill_value=9.0)
df3 = df.asfreq(freq='W', fill_value=9.0)
print(df2)


trades = pd.DataFrame({
    'time': pd.to_datetime(['20160525 13:30:00.023',
                            '20160525 13:30:00.038',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.048']),
    'ticker': ['MSFT', 'MSFT', 'GOOG', 'GOOG', 'AAPL'],
    'price': [51.95, 51.95, 720.77, 720.92, 98.00],
    'quantity': [75, 155, 100, 100, 100]},
    columns=['time', 'ticker', 'price', 'quantity'])
# print(trades)
quotes = pd.DataFrame({
    'time': pd.to_datetime(['20160525 13:30:00.023',
                            '20160525 13:30:00.023',
                            '20160525 13:30:00.030',
                            '20160525 13:30:00.041',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.049',
                            '20160525 13:30:00.072',
                            '20160525 13:30:00.075']),
    'ticker': ['GOOG', 'MSFT', 'MSFT', 'MSFT', 'GOOG', 'AAPL', 'GOOG', 'MSFT'],
    'bid': [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
    'ask': [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]},
    columns=['time', 'ticker', 'bid', 'ask'])

# print(quotes)
df_merge_asof = pd.merge_asof(trades, quotes,
                              on='time',
                              by='ticker')

# print(df_merge_asof)

# sof merge within 2ms between the quote time and the trade time
df_merge_asof_tolerance = pd.merge_asof(trades, quotes,
                                        on='time',
                                        by='ticker',
                                        tolerance=pd.Timedelta('2ms'))

# print(df_merge_asof_tolerance)


"""
OUTPUT: 
time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.048   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100


                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03


                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN


                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

"""
