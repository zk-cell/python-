#选择数据
import pandas as pd
import numpy as np

dates = pd.date_range('20210101',periods = 6,freq = 'D')
# print(dates)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns = ['A', 'B', 'C', 'D'])
print(df)
#对dataframe进行索引
# print(df['A'],df.B)
# print(df[0:3],df['20210101':'20210105'],sep = '\n\n')

#select by label: loc
#by row
# print(df.loc['20210103'])
#by column
# print(df.loc[:,['A','D']])
# print(df.loc[1:,['A','D']])

#select by position: iloc
# print(df.iloc[3][1])
# print(df.iloc[0:3,1:4])
# print(df.iloc[[1,3,5],[0,1]])

#mixed selection :ix    (已被弃用)


