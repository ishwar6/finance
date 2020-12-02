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
# print(df_row)
# print(df3)

# if: concat along columns
#df_col = pd.concat([df1, df2], axis=1)


# to merge along id
df_merge_col = pd.merge(df_row, df3, on='id')
# print(df_merge_col)

# to merge with separate keys: THEN PLZ Specify
df_merge_difkey = pd.merge(df_row, df3, left_on='id', right_on='id')


# ADDING NEW ROW
add_row = pd.Series(['10', 'X1', 'X2', 'X3'],
                    index=['id', 'Feature1', 'Feature2', 'Feature3'])

df_add_row = df_merge_col.append(add_row, ignore_index=True)


# JOIN
# full outer join
print(df1)
print(df2)
df_outer = pd.merge(df1, df2, on='id', how='outer')
# print(df_outer)
# suffix got appended to the column names to show which column came from which DataFrame

df_suffix = pd.merge(df1, df2, left_on='id', right_on='id',
                     how='outer', suffixes=('_left', '_right'))
# print(df_suffix)

# INNER JOIN
df_inner = pd.merge(df1, df2, on='id', how='inner')
# print(df_inner)

# RIGHT JOIN
df_right = pd.merge(df1, df2, on='id', how='right')
# print(df_right)

# TO join on the indexes or the row labels
df_index = pd.merge(df1, df2, right_index=True, left_index=True)
print(df_index)
