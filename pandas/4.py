#处理丢失数据
import pandas as pd
import numpy as np

dates = pd.date_range('20210101',periods = 6,freq = 'D')
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns = ['A', 'B', 'C', 'D'])
# print(df)

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
# print(df)

'''处理nan'''        
# .dropna(axis = 0/1,how = 'any'/'all')    去除含nan的行/列
#axis : {0 or 'index', 1 or 'columns'}, default 0 ;  any:某一行/列存在nan,remove那一行/列
# print(df.dropna(axis = 0, how = 'any', ))

'''
在nan处填数据:
.fillna(value = "要填充的数据",method = Literal['backfill', 'bfill', 'ffill', 'pad'],axis = 0/1)       
value : scalar, dict, Series, or DataFrame
    Value to use to fill holes (e.g. 0), alternately a dict/Series/DataFrame of values
specifying which value to use for each index (for a Series) or column (for a DataFrame). 
Values not in the dict/Series/DataFrame will not be filled. This value cannot be a list.
'''
# print(df.fillna(value = 0))

# values = {'B':'b','C':'c'}
# print(df.fillna(value = values))

#判断dataframe中是否存在nan(数据缺失)
#  .isnull 或搭配np.any
# print(df.isnull())

#np.any:判断是否存在某个数据,此处用于判断是否存在NAN
print(np.any(df.isnull() == True))



