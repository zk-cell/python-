#concat合并 
import pandas as pd
import numpy as np

# concatenating    pd.concat
df1 = pd.DataFrame(np.ones((3,4))*0,columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns = ['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns = ['a','b','c','d'])
# print(df1,df2,df3,sep = '\n')

'''
axis[0:'index',1:'column']    为0则index合并,column不变
'''
# result1 = pd.concat([df1,df2,df3], axis = 0)
# print(result1)

# result2 = pd.concat([df1,df2,df3], axis = 0,ignore_index=True)
# print(result2)

#    ignore_index:合并后index重新排序
df3 = pd.DataFrame(np.ones((3,4))*0,columns = ['a','b','c','d'],index = [1,2,3])
df4 = pd.DataFrame(np.ones((3,4))*1,columns = ['e','d','c','b'],index = [2,3,4])
print(df3,df4,sep = '\n')

#join:{'inner', 'outer'}, default 'outer'   处理index,'outer:空白处加上nan 'inner':只留下column共有的列
# result3 = pd.concat([df3,df4],join = 'outer')
# print(result3)
# result4 = pd.concat([df3,df4],join = 'inner',ignore_index=True)
# print(result4)

#join_axes:用于处理横向合并时index不同的问题  (已经弃用)  利用以下方法也行

'''appendc   合并单个/多个对象'''
result5 = df3.append(df4,ignore_index=True)
result6 = df3.append([df3,df4],ignore_index=True)
# print(result5)
# print(result6)

#dataframe与series 的合并      series是列向量,把index设置为dataframe的column即可
df5 = pd.Series([9,8,7,6],index = ['a','b','c','d'])
result7 = df3.append(df5,ignore_index=True)
# print(result7)


