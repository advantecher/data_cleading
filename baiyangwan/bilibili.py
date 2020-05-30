import pandas as pd

dfs = []
df0 = pd.read_excel(r'D:\testdata\2019-12-31.xls', sheet_name='臭氧发生', usecols='S, T, AN', header=None,
                    names=['水中余臭氧浓度(南)', '水中余臭氧浓度(北)', '臭氧破坏前浓度'],
                    );
df1 = pd.read_excel(r'D:\testdata\2019-12-31.xls', sheet_name='臭氧发生',
                    usecols='S, T, AN', skiprows=[0, 1, 2, 3, 4, 33, 34, 35, 36],
                    names=['水中余臭氧浓度(南)', '水中余臭氧浓度(北)', '臭氧破坏前浓度'],
                    header=None)
print("没有跳过行的size是{0}".format(df0.shape))
print("跳过行的size是{0}".format(df1.shape))
print("没跳过行：\n", df0)
print("跳过行：\n", df1)
# dfs.append(df1)

# df_concated = pd.concat(dfs)
# df_concated.to_excel(r'D:\testdata\all.xls', index=False, na_rep=0)
