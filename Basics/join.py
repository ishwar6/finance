# have a python dictonary
import pandas as pd
data1 = {
    'id': ['1', '2', '3', '4', '5'],
    'Feature1': ['A', 'C', 'E', 'G', 'I'],
    'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(data1)
# or
#df1 = pd.DataFrame(data1, columns=['id', 'Feature1', 'Feature2'])
# print(df1)

data2 = {
    'id': ['1', '2', '6', '7', '8'],
    'Feature1': ['K', 'M', 'O', 'Q', 'S'],
    'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(data2, columns=['id', 'Feature1', 'Feature2'])

data3 = {
    'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df3 = pd.DataFrame(data3, columns=['id', 'Feature3'])


# LETS CONCAT

df_row = pd.concat([df1, df2])
# vs
#df_row = pd.concat([df1, df2], ignore_index=True)


# instead of removing individual dataset index: use keys
df_row = pd.concat([df1, df2], keys=['x',
                                     'y'])
# or map the keys with dataframes at first place itself instead of in concat args :)
dict_keys = {'x': df1, 'y': df2}
df_row = pd.concat(dict_keys)
# Now retrieve with keys
print(df_row)
print(df3)

# if: concat along columns
#df_col = pd.concat([df1, df2], axis=1)


# to merge along id
df_merge_col = pd.merge(df_row, df3, on='id')
# print(df_merge_col)

# to merge with separate keys: THEN PLZ Specify
df_merge_difkey = pd.merge(df_row, df3, left_on='id', right_on='id')
