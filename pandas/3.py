#设置值
import pandas as pd
import numpy as np

dates = pd.date_range('20210101',periods = 6,freq = 'D')
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns = ['A', 'B', 'C', 'D'])
print(df)

#利用iloc改变值,类似列表
# df.iloc[1,2] = 'zk'
# print(df)

#利用loc改变值
# df.loc['20210105','D'] = 'aaa'
# print(df)

#利用逻辑语句改变值
# df[df.A > 5] = 6              #改变满足要求的所有列
# df.A[df.A > 5] = 9            #只改变一列
# print(df)

#创建新数据    series创建一个列向量
df['E'] = np.nan
df['F'] = pd.Series([1,2,3,4,5,6], index = pd.date_range('20210101',periods=6))
print(df)